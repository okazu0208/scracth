def main(event, context):
 import os
 os.system("pip install -U scratchattach")
 print("ok")
 import scratchattach as scratch3
 session = scratch3.Session(".eJxVT0tLxDAQ_i89a22TtCZ7WwVdEMQHHtxLmU2mbbZtUpqUguJ_dwJ72cPAzPfim99sDbg4mDDbZUEvEHX_tvimYNlN1sAa-yYJGmuIV0pwVtYlURFD1N4PNvk2vwxorg0n0AO65EoYumg1ROtdfiFC_oHzeAEfLmLK9bSQqVIMoJWmrYELlCVIbgrVSjBSSMPa3bZnffH1uIUXyZ6Oh9kfDQrx-X54DhQz-s66WzunJJnfFzmrc1mnhiO4boUu1T4DAeZMgG-infDHuwTvJ1yo190rbs03fXb9Vw-hJ5EApamiAcNrIzQXhRI0FTcay7biqICuos7-_gGaq3JW:1ppowi:RzXQOXVMhIb_NLKqxa4gUZDeLfk", username="scratchPro_02")
 conn = scratch3.CloudConnection(project_id = "838970827", username="scratchPro_02", session_id=".eJxVT0tLxDAQ_i89a22TtCZ7WwVdEMQHHtxLmU2mbbZtUpqUguJ_dwJ72cPAzPfim99sDbg4mDDbZUEvEHX_tvimYNlN1sAa-yYJGmuIV0pwVtYlURFD1N4PNvk2vwxorg0n0AO65EoYumg1ROtdfiFC_oHzeAEfLmLK9bSQqVIMoJWmrYELlCVIbgrVSjBSSMPa3bZnffH1uIUXyZ6Oh9kfDQrx-X54DhQz-s66WzunJJnfFzmrc1mnhiO4boUu1T4DAeZMgG-infDHuwTvJ1yo190rbs03fXb9Vw-hJ5EApamiAcNrIzQXhRI0FTcay7biqICuos7-_gGaq3JW:1ppowi:RzXQOXVMhIb_NLKqxa4gUZDeLfk")
 i = scratch3.get_var("838970827","e")
 if i == "1":
  f = open("cloud.txt","r")
  ii = f.readline()
  conn.set_var("e",ii)
 else:
  f = open("cloud.txt","w")
  f.write(str(i))
  f.close()
if __name__ == "__main__":
    main("event","context")