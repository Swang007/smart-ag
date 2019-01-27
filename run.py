from smartag import create_app
from smartag.database import db_session, init_db
from smartag.FarmServer import setupConnection
from smartag.ClientHandler import CHandler
from smartag.plants.models import Plant, PlantType
from threading import Thread
from random import randint

app = create_app()
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    

def int_to_pstring(a):
    if a == 0:
        return 'Basil'
    elif a == 1:
        return 'Cabbage'
    elif a == 2:
        return 'Strawberry'
    elif a == 3:
        return 'Rosemary'
    elif a == 4:
        return 'Spinnage'
    elif a == 5:
        return 'Broccoli'
    elif a == 6:
        return 'Wheat'
    elif a == 7:
        return 'Mint'

def func():
    clients = setupConnection(100, 8000)
    hit00 = False
    while 1:
        for c in clients:
            val = c.popQueue()
            if len(val) > 0:
                pid = f'{val[0]}-{val[5]}'
                if (pid == "0-0"):
                    print("0-0s:", hit00)
                    hit00 = True
                print(val)
                ran = randint(0, 7)
                p = Plant(pid=pid, uid=val[0], name=int_to_pstring(ran), water_level=val[1], chemical_a=randint(1, 100), 
                    chemical_b=randint(1, 100), growth_level=val[4], timestamp=val[5], state=val[6])
                if len(PlantType.query.filter(PlantType.name == int_to_pstring(ran)).all()) == 0:
                    pt = PlantType(int_to_pstring(ran))
                    db_session.add(pt)
                db_session.add(p)
                db_session.commit()

if __name__ == '__main__':
    init_db()

    server_thread = Thread(target=func)
    server_thread.start()

    app.run(debug=True)
    
