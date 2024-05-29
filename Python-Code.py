from ursina import*                                                                                                    # um die 3d Engine Ursiina zu importieren
from itertools import product                                                                                          # Tool welches Verschachelte Schleifen vereinfacht darstellen kann
import random 


start = ['W','W','W','W','G','G','O','O','B','B','R','R','G','G','O','O','B','B','R','R','Y','Y','Y','Y']              # farbfolge des Zauberwürfels zu Beginn

def eltern_kind_beziehung(achse, schicht):                                                                             # um eine Funktion welche die Eltern-Kind-Beziehung zwischen den Würfeln auf einer achse und einer Schicht zum Zentrum herstellt zu definieren 
    for c in würfel:
        c.position, c.rotation = round(c.world_position,1), c.world_rotation                                           # um die globale Postion des Würfels als neue lokale position festzulegen, damit wenn die Eltern_Kind-Beziehung aufgelöst wird die rotierten Würfel nicht wieder auf ihre uhrsprüngliche Position (lokal) zurückspringen 
        c.parent = scene                                                                                               # um die Eltern-Kind-beziehung aufzulösen, damit wenn das Zentrum wieder auf 0 zurückgesetzt wird, sich die davor mitrotierten Würfel nicht auch wieder mit zurück drehen 
    
    zentrum.rotation = 0                                                                                               # um das Rotationszentrum nach einer Rotation wieder auf 0 zurückzusetzten, sodass sich das ganze weiterdrehen lässt
    for c in würfel:                                                                                                   # um alle unten definierten Würfel durchzugehen
        if eval(f'c.position.{achse}') == schicht:                                                                     # eval() ist dazu da um in einen Befehl Variablen zu implementieren, indem er diesen als String betrachttet; f'' ist dazu da um die geschweiften Klammern aufzulösen und die jeweiligen Werte für Achse und Winkel einzusetzen; damit die darunter stehende Funktion ausgeführt wird wenn die Achsenposition des Würfels der Schicht entspricht
            c.parent = zentrum                                                                                         # um festzulegen dass das Zentrum die Eltern sind, also der Punkt um den sich die Würfel drehen

print('Würfel gelöst:','WWWWOOBBRRGGOOBBRRGGYYYY')

def input(key):                                                                                                        # damit die darunterstehende Funktion jedesmal aufgerufen wird, sobald eine Taste gedrückt wird
    if key not in rot_dict: return                                                                                     # damit falls die Taste nicht im Dictionary vorhanden ist, man aus diese Funktion wieder verlässt, ansonsten jedesmal Fehlermeldung wenn andere taste gedrückt wird
    achse, schicht, winkel = rot_dict[key]                                                                             # um die Achse, Schicht und den Winkel welcher zu der aus dem Dictionary gehörenden Taste gehört auszugeben
    eltern_kind_beziehung(achse, schicht)
    global start                                                                                                    # um die Eltern-Kind-Beziehung aufzurufen, undzwar das alle die auf dieser bestimmten Achse mit dieser bestimmten Schicht sind selektiert werden
    if held_keys['2']:                                                                                                 # um festzulegen das wenn die Taste 2 und eine andere Taste aus dem Dictionary gedrückt werden der untere Befehl ausgeführt wird
        eval(f'zentrum.animate_rotation_{achse}({2*winkel}, duration = 0.5)')                                          # eval() ist dazu da um in einen Befehl Variablen zu implementieren, indem er diesen als String betrachtet; f'' ist dazu da um die geschweiften Klammern aufzulösen und die jeweiligen Werte für Achse und Winkel einzusetzen; um alle selektierten Würfel, um das Zentrum, um 180°, mit einer Animation von 0,5s, um eine bestimmte Achse zu drehen
        p=key,'2'
        leer=' '
        p = "".join(x for x in p if x not in leer)
        print(p)
        zug.append(p)
        neu=[]
        if key =='u':                                                                                                  # um führ jede 180° Drehung die darauf passenede Farbdrehung zu implementieren sodass die Farbfolge korrekt ist
                neu=[start[2],start[3],start[0],start[1],
                    start[8],start[9],start[10],start[11],start[4],start[5],start[6],start[7],
                    start[12],start[13],start[14],start[15],start[16],start[17],start[18],start[19],
                    start[20],start[21],start[22],start[23]]
        elif key=='d':neu=[start[0],start[1],start[2],start[3],
                    start[4],start[5],start[6],start[7],start[8],start[9],start[10],start[11],
                    start[16],start[17],start[18],start[19],start[12],start[13],start[14],start[15],
                    start[22],start[23],start[20],start[21]]
        elif key=='r':neu=[start[0],start[1],start[21],start[22],
                    start[17],start[5],start[6],start[7],start[8],start[12],start[19],start[18],
                    start[9],start[13],start[14],start[15],start[16],start[4],start[11],start[10],
                    start[20],start[2],start[3],start[23]]
        elif key=='l':neu=[start[23],start[20],start[2],start[3],
                    start[4],start[16],start[15],start[14],start[13],start[9],start[10],start[11],
                    start[12],start[8],start[7],start[6],start[5],start[17],start[18],start[19],
                    start[1],start[21],start[22],start[0]]
        elif key=='f':neu=[start[21],start[1],start[2],start[20],
                    start[13],start[12],start[19],start[7],start[8],start[9],start[10],start[14],
                    start[5],start[4],start[11],start[15],start[16],start[17],start[18],start[6],
                    start[3],start[0],start[22],start[23]]
        elif key=='b':neu=[start[0],start[22],start[23],start[3],
                    start[4],start[5],start[6],start[18],start[17],start[16],start[15],start[11],
                    start[12],start[13],start[14],start[10],start[9],start[8],start[7],start[19],
                    start[20],start[21],start[1],start[2]]
        start.clear()
        start=neu
        print('Farbfolge:',start)
    elif held_keys['shift']:                                                                                           # um festzulegen das wenn die Taste shift und eine andere Taste aus dem Dictionary gedrückt werden der untere Befehl ausgeführt wird
        eval(f'zentrum.animate_rotation_{achse}({-winkel}, duration = 0.5)')                                            # eval() ist dazu da um in einen Befehl Variablen zu implementieren, indem er diesen als String betrachtet; f'' ist dazu da um die geschweiften Klammern aufzulösen und die jeweiligen Werte für Achse und Winkel einzusetzen; um alle selektierten Würfel, um das Zentrum, mit dem Uhrzeigersinn, um 90° Winkel, mit einer Animation von 0,5s, um eine bestimmte Achse zu drehen
        print(key.upper())
        zug.append(key.upper())
        neu=[]
        if key =='u':                                                                                                  # um führ jede 90° Drehung gegen den Uhrzeigersinn die darauf passenede Farbdrehung zu implementieren sodass die Farbfolge korrekt ist
                neu=[start[1],start[2],start[3],start[0],
                    start[6],start[7],start[8],start[9],start[10],start[11],start[4],start[5],
                    start[12],start[13],start[14],start[15],start[16],start[17],start[18],start[19],
                    start[20],start[21],start[22],start[23]]
        elif key=='d':neu=[start[0],start[1],start[2],start[3],
                    start[4],start[5],start[6],start[7],start[8],start[9],start[10],start[11],
                    start[14],start[15],start[16],start[17],start[18],start[19],start[12],start[13],
                    start[23],start[20],start[21],start[22]]
        elif key=='r':neu=[start[0],start[1],start[17],start[9],
                    start[2],start[5],start[6],start[7],start[8],start[22],start[18],start[10],
                    start[3],start[13],start[14],start[15],start[16],start[21],start[19],start[11],
                    start[20],start[4],start[12],start[23]]
        elif key=='l':neu=[start[8],start[16],start[2],start[3],
                    start[4],start[1],start[7],start[15],start[23],start[9],start[10],start[11],
                    start[12],start[0],start[6],start[14],start[20],start[17],start[18],start[19],
                    start[5],start[21],start[22],start[13]]
        elif key=='f':neu=[start[11],start[1],start[2],start[19],
                    start[12],start[4],start[3],start[7],start[8],start[9],start[10],start[21],
                    start[13],start[5],start[0],start[15],start[16],start[17],start[18],start[20],
                    start[6],start[14],start[22],start[23]]
        elif key=='b':neu=[start[0],start[10],start[18],start[3],
                    start[4],start[5],start[6],start[2],start[9],start[17],start[22],start[11],
                    start[12],start[13],start[14],start[1],start[8],start[16],start[23],start[19],
                    start[20],start[21],start[15],start[7]]
        start.clear()
        start=neu
        print('Farbfolge:',start)
    elif key=='n':                                                                                                     # um den zauberwürfel beim drücken der Taste n random verdrehen zu lassen
        m_last='h'
        for _ in range(0,11):                                                                                          # das 11 Drehungen ausgewällt werden
            m=random.choice(list(rot_dict.keys()))
            
            while m_last==m or m=='n' or m=='s' or m=='h':                                                             # um zu verhindern das 2-mal die selbe Drehung hintereinander ausgwählt wird
                m=random.choice(list(rot_dict.keys()))
                    
            achse, schicht, winkel = rot_dict[m]                                                                       # verdreht den Zauberwürfel
            eltern_kind_beziehung(achse, schicht)
            eval(f'zentrum.animate_rotation_{achse}({winkel}, duration = 0)')
            zug.append(m)
            neu=[]
            if m =='u':                                                                                                # um anschließend die Farbfolge zu erhalten
                neu=[start[3],start[0],start[1],start[2],
                    start[10],start[11],start[4],start[5],start[6],start[7],start[8],start[9],
                    start[12],start[13],start[14],start[15],start[16],start[17],start[18],start[19],
                    start[20],start[21],start[22],start[23]]
            elif m=='d':neu=[start[0],start[1],start[2],start[3],
                    start[4],start[5],start[6],start[7],start[8],start[9],start[10],start[11],
                    start[18],start[19],start[12],start[13],start[14],start[15],start[16],start[17],
                    start[21],start[22],start[23],start[20]]
            elif m=='r':neu=[start[0],start[1],start[4],start[12],
                    start[21],start[5],start[6],start[7],start[8],start[3],start[11],start[19],
                    start[22],start[13],start[14],start[15],start[16],start[2],start[10],start[18],
                    start[20],start[17],start[9],start[23]]
            elif m=='l':neu=[start[13],start[5],start[2],start[3],
                    start[4],start[20],start[14],start[6],start[0],start[9],start[10],start[11],
                    start[12],start[23],start[15],start[7],start[1],start[17],start[18],start[19],
                    start[16],start[21],start[22],start[8]]
            elif m=='f':neu=[start[14],start[1],start[2],start[6],
                    start[5],start[13],start[20],start[7],start[8],start[9],start[10],start[0],
                    start[4],start[12],start[21],start[15],start[16],start[17],start[18],start[3],
                    start[19],start[11],start[22],start[23]]
            elif m=='b':neu=[start[0],start[15],start[7],start[3],
                    start[4],start[5],start[6],start[23],start[16],start[8],start[1],start[11],
                    start[12],start[13],start[14],start[22],start[17],start[9],start[2],start[19],
                    start[20],start[21],start[10],start[18]]
            elif m =='u2':
                neu=[start[2],start[3],start[0],start[1],
                    start[8],start[9],start[10],start[11],start[4],start[5],start[6],start[7],
                    start[12],start[13],start[14],start[15],start[16],start[17],start[18],start[19],
                    start[20],start[21],start[22],start[23]]
            elif m=='d2':neu=[start[0],start[1],start[2],start[3],
                    start[4],start[5],start[6],start[7],start[8],start[9],start[10],start[11],
                    start[16],start[17],start[18],start[19],start[12],start[13],start[14],start[15],
                    start[22],start[23],start[20],start[21]]
            elif m=='r2':neu=[start[0],start[1],start[21],start[22],
                    start[17],start[5],start[6],start[7],start[8],start[12],start[19],start[18],
                    start[9],start[13],start[14],start[15],start[16],start[4],start[11],start[10],
                    start[20],start[2],start[3],start[23]]
            elif m=='l2':neu=[start[23],start[20],start[2],start[3],
                    start[4],start[16],start[15],start[14],start[13],start[9],start[10],start[11],
                    start[12],start[8],start[7],start[6],start[5],start[17],start[18],start[19],
                    start[1],start[21],start[22],start[0]]
            elif m=='f2':neu=[start[21],start[1],start[2],start[20],
                    start[13],start[12],start[19],start[7],start[8],start[9],start[10],start[14],
                    start[5],start[4],start[11],start[15],start[16],start[17],start[18],start[6],
                    start[3],start[0],start[22],start[23]]
            elif m=='b2':neu=[start[0],start[22],start[23],start[3],
                    start[4],start[5],start[6],start[18],start[17],start[16],start[15],start[11],
                    start[12],start[13],start[14],start[10],start[9],start[8],start[7],start[19],
                    start[20],start[21],start[1],start[2]]
            elif m =='U':
                neu=[start[1],start[2],start[3],start[0],
                    start[6],start[7],start[8],start[9],start[10],start[11],start[4],start[5],
                    start[12],start[13],start[14],start[15],start[16],start[17],start[18],start[19],
                    start[20],start[21],start[22],start[23]]
            elif m=='D':neu=[start[0],start[1],start[2],start[3],
                    start[4],start[5],start[6],start[7],start[8],start[9],start[10],start[11],
                    start[14],start[15],start[16],start[17],start[18],start[19],start[12],start[13],
                    start[23],start[20],start[21],start[22]]
            elif m=='R':neu=[start[0],start[1],start[17],start[9],
                    start[2],start[5],start[6],start[7],start[8],start[22],start[18],start[10],
                    start[3],start[13],start[14],start[15],start[16],start[21],start[19],start[11],
                    start[20],start[4],start[12],start[23]]
            elif m=='L':neu=[start[8],start[16],start[2],start[3],
                    start[4],start[1],start[7],start[15],start[23],start[9],start[10],start[11],
                    start[12],start[0],start[6],start[14],start[20],start[17],start[18],start[19],
                    start[5],start[21],start[22],start[13]]
            elif m=='F':neu=[start[11],start[1],start[2],start[19],
                    start[12],start[4],start[3],start[7],start[8],start[9],start[10],start[21],
                    start[13],start[5],start[0],start[15],start[16],start[17],start[18],start[20],
                    start[6],start[14],start[22],start[23]]
            elif m=='B':neu=[start[0],start[10],start[18],start[3],
                    start[4],start[5],start[6],start[2],start[9],start[17],start[22],start[11],
                    start[12],start[13],start[14],start[1],start[8],start[16],start[23],start[19],
                    start[20],start[21],start[15],start[7]]
            start.clear()
            start=neu
        print(zug)
        m_last=m
        print('Farbfolge:',start)
    elif key=='s':                                                                                                      # um den zauberwürfel in seine Ausgangsposition zurückzudrehen
            zug_U= list(reversed(zug))                                                                                  # um die Liste der Drehungen umzudrehen
            print('Umkehrung:',zug_U)
            for index, value in enumerate(zug_U):                                                                       # um Drehung in der Liste mit der jeweils entgegengesetzten zu vertauschen 
                if value == 'b':
                    zug_U[index] = 'B'
                elif value == 'B':
                    zug_U[index] = 'b'
                elif value == 'f':
                    zug_U[index] = 'F'
                elif value == 'F':
                    zug_U[index] = 'f'
                elif value == 'l':
                    zug_U[index] = 'L'
                elif value == 'L':
                    zug_U[index] = 'l'
                elif value == 'r':
                    zug_U[index] = 'R'
                elif value == 'R':
                    zug_U[index] = 'r'
                elif value == 'U':
                    zug_U[index] = 'u'
                elif value == 'u':
                    zug_U[index] = 'U'
                elif value == 'd':
                    zug_U[index] = 'D'
                elif value == 'D':
                    zug_U[index] = 'd'
            print('Lösung:',zug_U)
            for i in zug_U:                                                                                            # um den Zauberwürfel in seine Ausgangslage zurückzudrehen
                achse, schicht, winkel = rot_dict[i]
                eltern_kind_beziehung(achse, schicht)
                eval(f'zentrum.animate_rotation_{achse}({winkel}, duration = 0)')                                      
            zug.clear()
            zug_U.clear()
            start=['W','W','W','W','G','G','O','O','B','B','R','R','G','G','O','O','B','B','R','R','Y','Y','Y','Y']
            print('Würfel gelöst:',start)               
    else:                                                                                                              # um festzulegen das wenn nu eine Taste aus dem Dictionary gedrückt weird der untere Befehl ausgeführt wird
        eval(f'zentrum.animate_rotation_{achse}({winkel}, duration = 0.5)')                                            # eval() ist dazu da um in einen Befehl Variablen zu implementieren, indem er diesen als String betrachtet; f'' ist dazu da um die geschweiften Klammern aufzulösen und die jeweiligen Werte für Achse und Winkel einzusetzen; um alle selektierten Würfel, um das Zentrum, mit dem Uhrzeigersinn, um 90° Winkel, mit einer Animation von 0,5s, um eine bestimmte Achse zu drehen
        print(key)
        zug.append(key)
        neu=[]
        if key =='u':                                                                                                  # um führ jede 90° Drehung im Uhrzeigersinn die darauf passenede Farbdrehung zu implementieren sodass die Farbfolge korrekt ist
                neu=[start[3],start[0],start[1],start[2],
                    start[10],start[11],start[4],start[5],start[6],start[7],start[8],start[9],
                    start[12],start[13],start[14],start[15],start[16],start[17],start[18],start[19],
                    start[20],start[21],start[22],start[23]]
        elif key=='d':neu=[start[0],start[1],start[2],start[3],
                    start[4],start[5],start[6],start[7],start[8],start[9],start[10],start[11],
                    start[18],start[19],start[12],start[13],start[14],start[15],start[16],start[17],
                    start[21],start[22],start[23],start[20]]
        elif key=='r':neu=[start[0],start[1],start[4],start[12],
                    start[21],start[5],start[6],start[7],start[8],start[3],start[11],start[19],
                    start[22],start[13],start[14],start[15],start[16],start[2],start[10],start[18],
                    start[20],start[17],start[9],start[23]]
        elif key=='l':neu=[start[13],start[5],start[2],start[3],
                    start[4],start[20],start[14],start[6],start[0],start[9],start[10],start[11],
                    start[12],start[23],start[15],start[7],start[1],start[17],start[18],start[19],
                    start[16],start[21],start[22],start[8]]
        elif key=='f':neu=[start[14],start[1],start[2],start[6],
                    start[5],start[13],start[20],start[7],start[8],start[9],start[10],start[0],
                    start[4],start[12],start[21],start[15],start[16],start[17],start[18],start[3],
                    start[19],start[11],start[22],start[23]]
        elif key=='b':neu=[start[0],start[15],start[7],start[3],
                    start[4],start[5],start[6],start[23],start[16],start[8],start[1],start[11],
                    start[12],start[13],start[14],start[22],start[17],start[9],start[2],start[19],
                    start[20],start[21],start[10],start[18]]
        start.clear()
        start=neu
        print('Farbfolge:',start)
        
        
app= Ursina()                                                                                                          # Ursina unter variable app speicher
window.borderless = False                                                                                              # um das Fenster ein Rahmen zu geben, sodass man es rumschieben kann
window.size = (800,800)                                                                                                # um dem Fenster eine größe zu geben
window.position = (192, 108)                                                                                           # sodass das Fenster im Bildschirm liegt
EditorCamera()                                                                                                         # um eine Kamera festzulegen sodass man im Fenster zoomen und Objekte bewegen kann

zentrum = Entity()                                                                                                     # legt das Zentrum fest dadurch das keine Position festgelegt wurde, wird es auf Koordinaten (0,0,0) festgelegt


rot_dict = {'l':['x', -1, 90], 'L':['x', -1, -90], 'l2':['x', -1, 180], 'r':['x', 1, 90], 'R':['x', 1, -90], 'r2':['x', 1, 180],                                                                         # Dictionary welches für jede Taste die jeweilige Achse, Schicht nd Winkel bestimmt
            'd':['y', -1, 90], 'D':['y', -1, -90], 'd2':['y', -1, 180], 'u':['y', 1, 90], 'U':['y', 1, -90], 'u2':['y', 1, 180],
            'f':['z', -1, 90], 'F':['z', -1, -90], 'f2':['z', -1, 180], 'b':['z', 1, 90], 'B':['z', 1, -90], 'b2':['z', 1, 180],
            'n':['x',0,0],'s':['x',0,0]}

zug = []


würfel = []                                                                                                            # um eine Liste für die Würfel zu erstellen
for pos in product((-1,1),repeat=3):                                                                                   # um auf einem Koordinatensystem mit 3 Achsen die Koordinaten für jede Stelle festzulegen an der ein WÜrfel sein soll 
    würfel.append(Entity(model='Teil_46_model.obj', texture = 'Teil_46_texture.png', position=pos, scale=1))           # um an jeder Stelle einen Würfel nach dem Model des Teil_46 und mit der Farbe des Teil_46 zu haben, welcher 1 Einheit breit ist und in der Liste Würfel hinterlegt wird
             
app.run()                                                                                                              # bringt den Code zum laufen
