from api.rfb import check_engine_startup


class Engine:
    def engneStartUp(self, engine_type):
        print(f"Starting Up {engine_type} engine...")
        if check_engine_startup():
            print("continue...")
            return "Engine Started"