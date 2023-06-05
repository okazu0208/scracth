# セットアップ
import os
os.system("pip install -U scratchattach")
import datetime
import subprocess
import scratchattach as scratch3
#コロン
session = scratch3.Session(".eJxVT0tLxDAQ_i89a22TtCZ7WwVdEMQHHtxLmU2mbbZtUpqUguJ_dwJ72cPAzPfim99sDbg4mDDbZUEvEHX_tvimYNlN1sAa-yYJGmuIV0pwVtYlURFD1N4PNvk2vwxorg0n0AO65EoYumg1ROtdfiFC_oHzeAEfLmLK9bSQqVIMoJWmrYELlCVIbgrVSjBSSMPa3bZnffH1uIUXyZ6Oh9kfDQrx-X54DhQz-s66WzunJJnfFzmrc1mnhiO4boUu1T4DAeZMgG-infDHuwTvJ1yo190rbs03fXb9Vw-hJ5EApamiAcNrIzQXhRI0FTcay7biqICuos7-_gGaq3JW:1ppowi:RzXQOXVMhIb_NLKqxa4gUZDeLfk", username="scratchPro_02")
conn = scratch3.CloudConnection(project_id = "838970827", username="scratchPro_02", session_id=".eJxVT0tLxDAQ_i89a22TtCZ7WwVdEMQHHtxLmU2mbbZtUpqUguJ_dwJ72cPAzPfim99sDbg4mDDbZUEvEHX_tvimYNlN1sAa-yYJGmuIV0pwVtYlURFD1N4PNvk2vwxorg0n0AO65EoYumg1ROtdfiFC_oHzeAEfLmLK9bSQqVIMoJWmrYELlCVIbgrVSjBSSMPa3bZnffH1uIUXyZ6Oh9kfDQrx-X54DhQz-s66WzunJJnfFzmrc1mnhiO4boUu1T4DAeZMgG-infDHuwTvJ1yo190rbs03fXb9Vw-hJ5EApamiAcNrIzQXhRI0FTcay7biqICuos7-_gGaq3JW:1ppowi:RzXQOXVMhIb_NLKqxa4gUZDeLfk")
r = 1000
while r == 0:
 #main
 m = current_time.minute
 if m == 59:
  os.system("python AIpictures.py")
 #数える
 r - 1