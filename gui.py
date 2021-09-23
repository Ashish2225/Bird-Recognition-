import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy
#load the trained model to classify bird
from keras.models import load_model
model = load_model('bird_classifier.h5')

#dictionary to label all bird image class.
classes = { 1:'Finch Bird\n The smallest "classical" true finches are the Andean siskin (Spinus spinescens)\n at as little as 9.5 cm (3.8 in) and the lesser goldfinch (Spinus psaltria)\n at as little as 8 g (0.28 oz).\nThe largest species is probably the collared grosbeak (Mycerobas affinis) at up to 24 cm (9.4 in)\n and 83 g (2.9 oz), although larger lengths, to 25.5 cm (10.0 in) in the pine grosbeak\n (Pinicola enucleator), and weights, to 86.1 g (3.04 oz) in the evening grosbeak\n (Hesperiphona vespertina), have been recorded in species which are slightly smaller on average.',
            2:'Lark Bird\n Larks, which are part of the family Alaudidae,\n are small- to medium-sized birds,\n 12 to 24 cm (4.7 to 9.4 in) in length and 15 to 75 g (0.5 to 2.6 oz) in mass.\nLike many ground birds, most lark species have long hind claws,\n which are thought to provide stability while standing.\n Most have streaked brown plumage, some boldly marked with black or white.\n Their dull appearance camouflages them on the ground, \nespecially when on the nest. ',
            3:'Lalage Bird\n Lalage is a genus of passerine birds belonging to the cuckooshrike \nfamily Campephagidae, many of which are commonly known as trillers.\n There are about 18 species which occur in southern Asia and Australasia\n with a number of species on Pacific islands.\n They feed mainly on insects and fruit.\n They build a neat cup-shaped nest high in a tree.\nThey are fairly small birds, about 15 to 20 cm long.\n They are mainly black, grey and white in colour.',
            4:'Quetzal Bird\n Quetzals are fairly large (all over 32 cm or 13 inches long),\n slightly bigger than other trogon species. The resplendent quetzal is the national\n bird of Guatemala because of its vibrant colour.\nQuetzals have iridescent green or golden-green wing coverts,\n back, chest and head, with a red belly.\n They are strongly sexually dimorphic, and parts of the females\n plumage are brown or grey. These largely solitary birds feed on fruits,\n berries, insects and small vertebrates (such as frogs).',
            5:'Apalis Bird\n The apalises are small passerine birds belonging to the genus Apalis,\n in the family Cisticolidae. They are found in forest, \nwoodlands and scrub across most parts of sub-Saharan Africa.\n They are slender birds with long tails and have a slender bill for catching insects. \nThey are typically brown, grey or green above and several species have brightly coloured underparts.\n Males and females are usually similar in appearance but the males are sometimes brighter.',

            7:'Tody Bird\n The todies are a family, Todidae,\n of tiny Caribbean birds in the order Coraciiformes, \nwhich also includes the kingfishers, bee-eaters and rollers.\n The family has one living genus, Todus, and one genus known from\n the fossil record, Palaeotodus.\nTodies range in weight from 5 to 7 g and in length from 10 to 11.5 cm.\n They have colourful plumage, and resemble kingfishers in their general shape.\nThey have green heads, backs and wings, red throats  ',

            9:'Bluejay Bird \nThe blue jay measures 22–30 cm (9–12 in) from bill to tail and weighs 70–100 g (2.5–3.5 oz),\n with a wingspan of 34–43 cm (13–17 in).\n Consistent with Bergmanns rule, jays from Connecticut averaged 92.4 g (3.26 oz) in mass,\n while jays from warmer southern Florida averaged 73.7 g (2.60 oz).\n When the bird is feeding among other jays or resting,\n the crest is flattened on the head.',
           10:'Humming Bird\n Hummingbirds are small birds of the family Trochilidae.\n They are among the smallest of birds: most species measure 7.5–13 cm (3–5 in).\n The smallest living bird species is the 2–5 cm Bee Hummingbird.\n They can hover in mid-air by rapidly flapping their wings\n 12–80 times per second (depending on the species).\nThey are also the only group of birds able to fly backwards.\n Their rapid wing beats do actually hum.\n They can fly at speeds over 15 m/s (54 km/h, 34 mi/h).',

           12:'Anhinga Bird\n The A. anhinga species is a large bird and measures approximately 89 cm (35 in) in length, \nwith a range of 75–95 cm (30–37 in), and a 1.14 m (3.7 ft) wingspan.\nThe male is a glossy black-green with the wings, base of wings,\n and tail a glossy black-blue.The tip of the tail has white feathers.',
           13:'Aracari Bird\n They are brightly plumaged and have enormous, contrastingly patterned bills. \nThese birds are residents in forests and woodlands in the Neotropics.\n Some species of aracaris are unusual for toucans in that they roost socially\n throughout the year, up to six adults and fledged young sleeping in the same\n hole with tails folded over their backs.',
           14:'Goldcrest Bird\n The goldcrest is the smallest European bird, 8.5–9.5 cm (3.3–3.7 in)\n in length, with a 13.5–15.5 cm (5.3–6.1 in) wingspan and a weight\n of 4.5–7.0 g (0.16–0.25 oz). It is similar in appearance to a warbler,\n with olive-green upper-parts, buff-white underparts, two white wing bars,\n and a plain face with conspicuous black irises.\n The small, thin bill is black, and the legs are dark flesh-brown.',
           15:'Sparrow Bird\nSparrows are small birds. \nThey are between 11–18 centimeters long.\n They can weigh between 13–42 grams. \nThey are usually brown and gray. \nThey have short tails and small, strong beaks.\n Most sparrows eat seeds or small insects. \nSparrows are social birds and they live in flocks (groups).',
           16:'Partridge Bird\n Partridges are medium-sized non-migratory birds,\n with a wide native distribution throughout Europe, Asia, and parts of Africa.\n They are sometimes grouped in the Perdicinae subfamily of the Phasianidae\n (pheasants, quail, etc.). However, molecular research suggests that partridges are not\n a distinct taxon within the family Phasianidae,\n but that some species are closer to the pheasants,\n while others are closer to the junglefowl.',

           19:'Brahminy Bird\n The brahminy kite (Haliastur indus), formerly known as the red-backed sea-eagle in Australia,\n is a medium-sized bird of prey in the family Accipitridae,\n which also includes many other diurnal raptors, such as eagles,\n buzzards, and harriers. They are found in the Indian subcontinent,\n Southeast Asia, and Australia. They are found mainly on the coast and in inland wetlands,\n where they feed on dead fish and other prey.\n Adults have a reddish-brown body plumage contrasting with their\n white head and breast which make them easy to distinguish\n from other birds of prey.',

           21:'Black Baza Bird\n The black baza (Aviceda leuphotes) is a small sized bird of prey \nfound in the forests of the Northeast India, the eastern Himalayas, \nChina and Southeast Asia. Many populations are migratory. \nThe races in the Indian region are migratory, wintering in the south\n of the Peninsula and Sri Lanka. The black bazas have short,\n stout legs and feet with strong talons. A prominent crest is a feature of the bazas.\n They are found in dense forest often in small groups. \nThey are also known to spend a lot of time perching on bare branches of tall \ntrees rising above the forest canopy.',
           22:'Darter Bird\n The Oriental darter (Anhinga melanogaster) is a water bird of tropical South Asia and Southeast Asia.\n It has a long and slender neck with a straight, pointed bill and, like the cormorant,\n it hunts for fish while its body is submerged in water.\n It spears a fish underwater, bringing it above the surface,\n tossing and juggling it before swallowing the fish head first.\n The body remains submerged as it swims, \nand the slender neck alone is visible above the water,\n which accounts for the colloquial name of snakebird.',
           23:'Gannet Bird\n Gannets are large white birds with yellowish head, black-tipped wings\n and long bills. Northern gannets are the largest seabirds in the North Atlantic,\n having a wingspan of up to 2 m (6.6 ft).\n The other two species occur in the temperate seas around southern Africa,\n southern Australia, and New Zealand.\nGannets are colonial breeders on islands and coasts, normally\n laying one chalky-blue egg. ',
           24:'Sandpiper Bird\n The name sandpiper refers particularly to several species of small\n to middle-sized birds, about 15 to 30 cm (6 to 12 inches) long,\n that throng sea beaches and inland mud flats during migration.\n Sandpipers have moderately long bills and legs,\n long, narrow wings, and fairly short tails.\nSandpipers have long bodies and legs, and narrow wings.\n Most species have a narrow bill, but otherwise the form and length are quite variable.\n They are small to medium-sized birds, measuring 12 to 66 cm (4.7–26.0 in) in length.\n The bills are sensitive,\n allowing the birds to feel the mud and sand as they probe for food. ',

           26:'Curlew Bird\n They are one of the most ancient lineages of scolopacid waders,\n together with the godwits which look similar but have straight bills.\n Curlews feed on mud or very soft ground,\n searching for worms and other invertebrates with their long bills.\n They will also take crabs and similar items.',
           27:'Barbet Bird \nBarbets are named for the bristles at the bases of their stout, sharp bills. \nThey are big-headed, short-tailed birds, 9–30 cm (3.5–12 inches) long, greenish or brownish, \nwith splashes of bright colours or white. \nThe smallest barbets are known as tinkerbirds. \nBarbets sit stolidly in treetops when not feeding on insects, \nlizards, birds’ eggs, fruit, and berries. ',

           29:'Branta Bird\n The Canada goose (Branta canadensis) is a large wild goose with a black head and\n neck, white cheeks, white under its chin, and a brown body.\n It is native to the Arctic and temperate regions of North America,\n and its migration occasionally reaches northern Europe.\n It has been introduced to the United Kingdom, Ireland, Finland, Sweden, Denmark,\n New Zealand, Japan, Argentina, Chile, and the Falkland Islands.\n Like most geese, the Canada goose is primarily herbivorous and normally migratory.\n it tends to be found on or close to fresh water.',
           30:'Kea Bird\n The kea nests in burrows or crevices among the roots of trees.\n Kea are known for their intelligence and curiosity,\n both vital to their survival in a harsh mountain environment.\n Kea can solve logical puzzles, such as pushing and pulling things \nin a certain order to get to food,\n and will work together to achieve a certain objective.\nThe kea is a large parrot about 48 cm (19 in)\n long and weighs between 800 grams (1.8 lb) and 1 kilogram (2.2 lb).\n It has mostly olive-green plumage with a grey beak having a long,\n narrow, curved upper beak.',
           31:'Jacana Bird\n Jacana, also called lily-trotter or lotus bird,\n any of several species of water birds belonging to the family\n Jacanidae of the order Charadriiformes.\n Jacanas are uniquely equipped with long straight claws for walking on\n floating vegetation. Like certain plovers,\n some jacanas have wing spurs.',
           32:'Kite Bird\n Kite, any of numerous birds of prey belonging to one\n of three subfamilies (Milvinae, Elaninae, Perninae) of the family Accipitridae.\n Typically, a kite is lightly built, with a small head,\n partly bare face, short beak, and long narrow wings and tail.\n Kites occur worldwide in warm regions.\n',
           33:'Bulbul Bird\n Bulbul, any of about 140 species of birds of the family Pycnonotidae (order Passeriformes)\n of Africa and Asia, including some called greenbuls and brownbuls.\n ... Members range in size from 14 to 28 cm (5.5 to 11 inches) long.\n They are active, noisy, plain-coloured birds that sometimes damage orchards.',

           35:'Nighthawk Bird\n Nighthawks are medium-sized birds with long wings,\n short legs, and very short bills.\n They usually nest on the ground. They feed on flying insects.\n The least nighthawk, at 16 centimetres (6.3 in) and 23 grams (0.81 oz),\n is the smallest of all Caprimulgiformes.\nNighthawks have small feet, of little use for walking,\n and long pointed wings. Their soft plumage is cryptically coloured to\n resemble bark or leaves. Some species perch facing along a branch,\n rather than across it as birds usually do.',

           37:'Wrens Bird\n Wrens are a family of brown passerine birds in the predominantly \nNew World family Troglodytidae. The family includes 88 species divided into 19 genera.\n ... Wrens have short wings that are barred in most species,\n and they often hold their tails upright.\nWrens are medium-small to very small birds.\n The Eurasian wren is among the smallest birds in its range,\n while the smaller species from the Americas are among \nthe smallest passerines in that part of the world.',

           39:'Phoebe Bird\n The Eastern Phoebe is a plump songbird with a medium-length tail.\n It appears large-headed for a bird of its size.\n The head often appears flat on top,\n but phoebes sometimes raise the feathers up into a peak.\n Like most small flycatchers, they have short,\n thin bills used for catching insects.\nThey prefer semi-open or open areas.\n These birds wait on a perch and then catch insects.\n Their nest is an open cup sometimes placed on man-made structures.\nThey often slowly lower and raise their tails while perched.',
           40:'Canary Bird\n Canaries were first bred in captivity in the 17th century,\n having been brought to Europe by Spanish sailors.\n This bird became expensive and fashionable to breed in courts \nof Spanish and English kings.\n Monks started breeding them and only sold the males (which sing).\nThis kept the birds in short supply and drove the price up.\n Eventually, Italians obtained hens and were able to breed the birds.',
           41:'Albatross Bird \nAlbatrosses are very large seabirds in the family Diomedeidae.\n They range widely in the Southern Ocean and the North Pacific.\n They are absent from the North Atlantic, \nalthough fossil remains show they once occurred there and occasional vagrants are found.',
           42:'Avocet Bird\n Avocets have long legs and they sweep their long, thin, \nupcurved bills from side to side when feeding in the brackish or\n saline wetlands they prefer. The plumage is pied, sometimes also with some red.',
           43:'Yuhina Bird\n Yuhina (from yuhin, Nepali for Y. gularis) is a genus of bird\n which is placed in the family Zosteropidae by recent molecular\n phylogeny studies or included within the Old World babbler family, Timaliidae.'}
                 
#initialise GUI
top=tk.Tk()
top.geometry('950x750')
top.title('Bird Recognition Project')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Identify Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Know Your Bird Name & Details",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
