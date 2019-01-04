#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from colorama import init, Fore, Back, Style
import credentials
import os
import dataToCsv
import os.path

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    cont = 0
    list_tweet = []
    file_name = input(Fore.RED +"\n** No poner la extensión en el nombre **\n** Si el archivo ya existe los datos se añadirán al mismo **\n\n"+ Fore.YELLOW + "Introduce el nombre para tu archivo CSV: ")

    def on_status(self, status):

            if hasattr(status, 'retweeted_status'):
                try:
                    data = status.retweeted_status.extended_tweet["full_text"]
                except:
                    data = status.retweeted_status.text
            else:
                try:
                    data = status.extended_tweet["full_text"]
                except AttributeError:
                    data = status.text

            if data not in self.list_tweet:
                self.list_tweet.append(data)
                dataToCsv.write(self.file_name,data, self.cont);
                self.cont +=  1
                if os.name == "posix":
                    os.system("clear")
                elif os.name == ("ce", "nt", "dos"):
                    os.system("cls")
                print(Fore.GREEN + Style.BRIGHT + str(self.cont) + " tweets encontrados" + "\n")
                print(Fore.RED + Style.BRIGHT + " Pulsa la tecla control + c para detener la búsqueda \n")
                print(Fore.MAGENTA + "  Los resultados se escribirán en el archivo " + str(self.file_name) + ".csv")
                


    def on_error(self, status):
        print(status)
    

        

if __name__ == '__main__':
    def patrons(str):
        

        patrons = patron.split(",")
        return patrons

    try:
        
        l = StdOutListener()
        auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
        auth.set_access_token(credentials.access_token, credentials.access_token_secret)
        stream = Stream(auth, l, tweet_mode='extended')

        # annadimos las palabras clave por las que queremos filtrar los tweets
        patron = input(Fore.MAGENTA + "\n introduce las palabras, hastag, etc por las que quieres busca, si es más de una palabra separelas por comas: ")

        print(Fore.GREEN + "\nBusqueremos las siguientes coincidencias", patrons(patron))

        stream.filter(track=patrons(patron))
    except KeyboardInterrupt:
        print('\n\n  ' + Fore.GREEN + 'La búsqueda finalizó correctamente. \n Comprueba tus resultados en el archivo CSV resultante.')
        stream.disconnect()



    
