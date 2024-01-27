from ursina import*                                                                                                    # um die 3d Engine Ursiina zu importieren
from itertools import product                                                                                          # Tool welches Verschachelte Schleifen vereinfacht darstellen kann

def eltern_kind_beziehung(achse, schicht):                                                                             # um eine Funktion welche die Eltern-Kind-Beziehung zwischen den Würfeln auf einer achse und einer Schicht zum Zentrum herstellt zu definieren 
    for w in würfel:
        w.position, w.rotation = round(w.world_position,1), w.world_rotation                                           # um die globale Postion des Würfels als neue lokale position festzulegen, damit wenn die Eltern_Kind-Beziehung aufgelöst wird die rotierten Würfel nicht wieder auf ihre uhrsprüngliche Position (lokal) zurückspringen 
        w.parent = scene                                                                                               # um die Eltern-Kind-beziehung aufzulösen, damit wenn das Zentrum wieder auf 0 zurückgesetzt wird, sich die davor mitrotierten Würfel nicht auch wieder mit zurück drehen 
    
    zentrum.rotation = 0                                                                                               # um das Rotationszentrum nach einer Rotation wieder auf 0 zurückzusetzten, sodass sich das ganze weiterdrehen lässt
    for w in würfel:                                                                                                   # um alle unten definierten Würfel durchzugehen
        if eval(f'w.position.{achse}') == schicht:                                                                     # eval() ist dazu da um in einen Befehl Variablen zu implementieren, indem er diesen als String betrachttet; f'' ist dazu da um die geschweiften Klammern aufzulösen und die jeweiligen Werte für Achse und Winkel einzusetzen; damit die darunter stehende Funktion ausgeführt wird wenn die Achsenposition des Würfels der Schicht entspricht
            w.parent = zentrum                                                                                         # um festzulegen dass das Zentrum die Eltern sind, also der Punkt um den sich die Würfel drehen


def input(key):                                                                                                        # damit die darunterstehende Funktion jedesmal aufgerufen wird, sobald eine Taste gedrückt wird
    if key not in rot_dict: return                                                                                     # damit falls die Taste nicht im Dictionary vorhanden ist, man aus diese Funktion wieder verlässt, ansonsten jedesmal Fehlermeldung wenn andere taste gedrückt wird
    achse, schicht, winkel = rot_dict[key]                                                                             # um die Achse, Schicht und den Winkel welcher zu der aus dem Dictionary gehörenden Taste gehört auszugeben
    eltern_kind_beziehung(achse, schicht)                                                                              # um die Eltern-Kind-Beziehung aufzurufen, undzwar das alle die auf dieser bestimmten Achse mit dieser bestimmten Schicht sind selektiert werden
    if held_keys['2']:                                                                                                 # um festzulegen das wenn die Taste 2 und eine andere Taste aus dem Dictionary gedrückt werden der untere Befehl ausgeführt wird
        eval(f'zentrum.animate_rotation_{achse}({2*winkel}, duration = 0.5)')                                          # eval() ist dazu da um in einen Befehl Variablen zu implementieren, indem er diesen als String betrachtet; f'' ist dazu da um die geschweiften Klammern aufzulösen und die jeweiligen Werte für Achse und Winkel einzusetzen; um alle selektierten Würfel, um das Zentrum, um 180°, mit einer Animation von 0,5s, um eine bestimmte Achse zu drehen
    elif held_keys['shift']:                                                                                           # um festzulegen das wenn die Taste shift und eine andere Taste aus dem Dictionary gedrückt werden der untere Befehl ausgeführt wird
        eval(f'zentrum.animate_rotation_{achse}({-winkel}, duration = 0.5)')                                           # eval() ist dazu da um in einen Befehl Variablen zu implementieren, indem er diesen als String betrachtet; f'' ist dazu da um die geschweiften Klammern aufzulösen und die jeweiligen Werte für Achse und Winkel einzusetzen; um alle selektierten Würfel, um das Zentrum, gegen den Uhrzeigersinn, um 90°, mit einer Animation von 0,5s, um eine bestimmte Achse zu drehen
    else:                                                                                                              # um festzulegen das wenn nu eine Taste aus dem Dictionary gedrückt weird der untere Befehl ausgeführt wird
        eval(f'zentrum.animate_rotation_{achse}({winkel}, duration = 0.5)')                                            # eval() ist dazu da um in einen Befehl Variablen zu implementieren, indem er diesen als String betrachtet; f'' ist dazu da um die geschweiften Klammern aufzulösen und die jeweiligen Werte für Achse und Winkel einzusetzen; um alle selektierten Würfel, um das Zentrum, mit dem Uhrzeigersinn, um 90° Winkel, mit einer Animation von 0,5s, um eine bestimmte Achse zu drehen

app= Ursina()                                                                                                          # Ursina unter variable app speicher
window.borderless = False                                                                                              # um das Fenster ein Rahmen zu geben, sodass man es rumschieben kann
window.size = (800,800)                                                                                                # um dem Fenster eine größe zu geben
window.position = (192, 108)                                                                                           # sodass das Fenster im Bildschirm liegt
EditorCamera()                                                                                                         # um eine Kamera festzulegen sodass man im Fenster zoomen und Objekte bewegen kann

zentrum = Entity()                                                                                                     # legt das Zentrum fest dadurch das keine Position festgelegt wurde, wird es auf Koordinaten (0,0,0) festgelegt

rot_dict = {'l':['x', -1, 90], 'r':['x', 1, 90],                                                                       # Dictionary welches für jede Taste die jeweilige Achse, Schicht nd Winkel bestimmt
            'd':['y', -1, 90], 'u':['y', 1, 90],
            'f':['z', -1, 90], 'b':['z', 1, 90],}

würfel = []                                                                                                            # um eine Liste für die Würfel zu erstellen
for pos in product((-1,1),repeat=3):                                                                                   # um auf einem Koordinatensystem mit 3 Achsen die Koordinaten für jede Stelle festzulegen an der ein WÜrfel sein soll 
    würfel.append(Entity(model='Teil_46_model.obj', texture = 'Teil_46_texture.png', position=pos, scale=1))           # um an jeder Stelle einen Würfel nach dem Model des Teil_46 und mit der Farbe des Teil_46 zu haben, welcher 1 Einheit breit ist und in der Liste Würfel hinterlegt wird
     
app.run()                                                                                                              # bringt den Code zum laufen
