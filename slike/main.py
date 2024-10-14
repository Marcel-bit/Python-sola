# Naloge za obdelavo slik s knjižnico Pillow

# Opomba: Za vsako funkcijo, ki spreminja sliko, naj se rezultat shrani
# pod imenom "originalnoIme_opisSpremembe.png" v isti mapi kot originalna slika.

from PIL import Image, ImageOps, ImageFont, ImageDraw
from pytesseract import pytesseract 



def grayscale(image_path):
    """
    Funkcija pretvori barvno sliko v črno-belo.
    
    Parametri:
    image_path (str): Pot do izvirne slike
    
    Izhod:
    Shranjena črno-bela slika
    """
    # KODA

    im1 = Image.open(image_path)

    im2 = ImageOps.grayscale(im1) 
    im2.show()

def text_to_image(image_path, text, position, font_size=24, font_color=(255, 255, 255)):
    """
    Funkcija doda besedilo na sliko.
    
    Parametri:
    image_path (str): Pot do izvirne slike
    text (str): Besedilo za dodajanje
    position (tuple): Koordinate (x, y) za postavitev besedila
    font_size (int): Velikost pisave
    font_color (tuple): RGB barva pisave
    
    Izhod:
    Shranjena slika z dodanim besedilom
    """
    # KODA
    image = Image.open(image_path)

    watermark_image = image.copy()

    draw = ImageDraw.Draw(watermark_image)

    font = ImageFont.truetype("font/calibri.ttf", font_size)

    draw.text(position, text, font_color, font=font)

    watermark_image.show()

def logo_to_image(image_path, logo_path, position, scale=0.1, folder = None):
    """
    Funkcija doda logotip na sliko na določeno pozicijo.
    
    Parametri:
    image_path (str): Pot do izvirne slike
    logo_path (str): Pot do logotipa
    position (str): Pozicija logotipa (left, right, center, leftUp, rightUp, centerUp, leftDown, rightDown, centerDown)
    scale (float): Velikost logotipa glede na velikost slike (0.0 - 1.0)
    folder (str): Če podana pot mape, se logo doda vsem slikam v podani mapi. Tu se se slike shranijo v mapo "dodan logo".
    
    Izhod:
    Shranjena slika z dodanim logotipom
    if folder: logotip dodan na vse slke v podmapo "dodan logo"
    """
    # KODA
    im1 = Image.open(image_path)
    im2 = Image.open(logo_path)
    w1, h1 = im1.size
    w2, h2 = im2.size
    center_x, center_y = (w1/2), (h1/2)
    im2_x = center_x - (w2/2)
    im2_y = center_y - (h2/2)


    pos = {
        'left':(0, int(im2_x)), 
        'right':(int(w1-w2), int(im2_x)), 
        'center':(int(im2_y), int(im2_x)), 
        'leftUp':(0, 0), 
        'rightUp':(int(w1-w2), 0), 
        'centerUp':(int(im2_y), 0), 
        'leftDown':(0, h1 - h2), 
        'rightDown':(int(w1-w2), h1 - h2), 
        'centerDown':(int(im2_y), h1 - h2)
    }
    print(w1, h1)
    print(w2, h2)

    back_im = im1.copy()
    back_im.paste(im2, pos['centerDown'])
    back_im.show()


    #back_im.save('data/dst/rocket_pillow_paste_pos.jpg', quality=95)

def my_filter(image_path, intensity=0.5):
    """
    Funkcija ustvari učinek filtra na sliki.
    
    Parametri:
    image_path (str): Pot do izvirne slike
    intensity (float): Intenzivnost učinka (0.0 - 1.0)
    
    Izhod:
    Shranjena slika s filtrom
    """
    # KODA, filter je lahko čisto poljuben!
    pass

def merge_images(folder_path, rows=1, cols=1):
    """
    Funkcija združi vse slike iz podane mape v eno samo sliko.
    
    Parametri:
    folder_path (str): Pot do mape s slikami
    rows (int): Število vrstic v končni sliki (opcijsko), če ni podano je default = 1
    cols (int): Število stolpcev v končni sliki (opcijsko), če ni podano je default = 1
    
    Izhod:
    Shranjena združena slika
    """
    # KODA
    pass

def random_quote(image_path, quote_file, font_size=24, font_color=(255, 255, 255)):
    """
    Funkcija doda naključni citat na sliko.
    
    Parametri:
    image_path (str): Pot do izvirne slike
    quote_file (str): Pot do datoteke s citati
    font_size (int): Velikost pisave
    font_color (tuple): RGB barva pisave
    
    Izhod:
    Shranjena slika z dodanim citatom
    """
    # KODA
    pass



def blur_faces(image_path, blur_factor=15):
    """
    Funkcija zamegli obraze na sliki.
    Opomba: Ta funkcija bo potrebovala zunanjo knjižnico za zaznavanje obrazov.
    
    Parametri:
    image_path (str): Pot do izvirne slike
    blur_factor (int): Stopnja zameglitve (višja vrednost = več zameglitve)
    
    Izhod:
    Shranjena slika z zamagljenimi obrazi
    """
    # KODA
    pass

def collage(image_paths, output_size=(1000, 1000), shape='grid'):
    """
    Funkcija ustvari kolaž iz podanih slik.
    
    Parametri:
    image_paths (list): Seznam poti do slik
    output_size (tuple): Velikost končnega kolaža (širina, višina)
    shape (str): Oblika kolaža ('grid', 'random', 'circle',...zberi sam opcije)
    
    Izhod:
    Shranjena slika kolaža
    """
    # KODA
    pass

# Dodatne pomožne funkcije po potrebi (potrebno za vse točke)
def save():
    pass
# Testni klici funkcij (zakomentirani)
if __name__ == "__main__":
    imagePath1="./slike/lenna.png"
    logoPath2="./slike/wallstreet.jpeg"
    #grayscale(imagePath1)
    #text_to_image(imagePath1, "Primer besedila", (10, 10))
    logo_to_image(imagePath1, logoPath2, "center")
    # my_filter("pot/do/slike.jpg", intensity=0.7)
    # merge_images("pot/do/mape/s/slikami")
    # random_quote("pot/do/slike.jpg", "pot/do/citatov.txt")
    # blur_faces("pot/do/slike.jpg")
    # collage(["pot/do/slike1.jpg", "pot/do/slike2.jpg", "pot/do/slike3.jpg"])
    pass
