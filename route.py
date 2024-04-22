from flask import render_template, request, Flask, make_response
import cevaplar
import sourcepush
from sourcepush import demand
import statics

app = None
terminal_content1 = {
    1: [{
        "id":
        "a1",
        'hyper text':
        '''<pre>Let AB be the given finite straight-line.So it is required to construct an equilateral
triangle on the straight-line AB.
Let the circle BCD with center A and radius <input type="text" name="" value="" class="panelelement">
</pre>
'''
    }],
    2: [{
        "id": "a2",
        'hyper text': "<h3>ww</h3>"
    }]
}


def set_app(appx):
  global app
  app = appx
  if app != None:

    @app.route("/")
    def main():
      return render_template("main.html")

    @app.route("/proje")
    def proje():
      return render_template("Bio.html")

    @app.route("/Q/<string:onerme>")
    def Q(onerme):
      q1 = list(range(len(cevaplar.q[int(onerme)]) +
                      1))[1:len(cevaplar.q[int(onerme)]) + 1]
      q2 = []
      for i in q1:
        q2.append("q" + str(i))
      return render_template("Q.html",
                             X=onerme,
                             onerme="onermeler/" + onerme + ".png",
                             terminal_content=statics.getelement(onerme),
                             rq1=True,
                             pri=int(onerme) - 1,
                             pos=int(onerme) + 1,
                             cevaplar=str(cevaplar.q[int(onerme)]),
                             inputs=q2)

    @app.route("/Q/")
    def QW():
      return render_template("Q.html", )
