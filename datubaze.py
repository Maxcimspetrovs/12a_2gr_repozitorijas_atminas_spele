import sqlite3


def get_top_result():
  conn = sqlite3.connect('datubaze.db')
  c = conn.cursor()
  c.execute("SELECT * FROM rezultati")
  rezultati = c.fetchall()
  conn.close()
  dati = [
    {"id": r[0], "vards": r[1], "rezultats": r[2], "laiks": [3], "datums": r[4]}
    for r in rezultati
  ]

  return dati

def pievienot(dati):
  conn = sqlite3.connect('datubaze.db')
  c = conn.cursor()
  c.execute("""
INSERT INTO rezultati (vards, rezultats, laiks, datums) VALUES (?, ?, ?, ?)
""", (dati["vards"], dati["rezultati"], dati["laiks"], dati["datums"]))
  conn.commmit()
  conn.close()