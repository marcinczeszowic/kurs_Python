'''
+ dodawanie
- odejmowanie
* mnozenie
/ dzielenie
() - jak w matematyce kieruja kolejnoscia dzialania
** potega
// dzielenie w "dół" - zaokrąglanie w dół
% modula ( reszta z dzielenia )
'''

VAT = 23
obliczonyVAT = (1 + VAT / 100)

cenaNettoJava = 10
cenaNettoAjax = 20


cenaBruttoJava = cenaNettoJava * obliczonyVAT
cenaBruttoAjax = cenaNettoAjax * obliczonyVAT

print(cenaBruttoJava)
print(cenaBruttoAjax)