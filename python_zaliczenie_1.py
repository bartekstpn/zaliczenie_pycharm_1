kwota_początkowa = 12000
inflacja_styczeń_2022 = 1.59282448436825
inflacja_luty_2022 = -0.453509101198007
inflacja_marzec_2022 = 2.32467171712441
inflacja_kwiecień_2022 = 1.26125440724877
inflacja_maj_2022 = 1.78252628571251
inflacja_czerwiec_2022 = 2.32938454145522
inflacja_lipiec_2022 = 1.50222984223283
inflacja_sierpień_2022 = 1.78252628571251
inflacja_wrzesień_2022 = 2.32884899407637
inflacja_październik_2022 = 0.616921348207244
inflacja_listopad_2022 = 2.35229588637833
inflacja_grudzień_2022 = 0.337779545187098
inflacja_styczeń_2023 = 1.57703524727525
inflacja_luty_2023 = -0.292781442607648
inflacja_marzec_2023 = 2.48619659017508
inflacja_kwiecień_2023 = 0.267110317834564
inflacja_maj_2023 = 1.41795267229799
inflacja_czerwiec_2023 = 1.05424326726375
inflacja_lipiec_2023 = 1.4805201044812
inflacja_sierpień_2023 = 1.57703524727525
inflacja_wrzesień_2023 = -0.0774206903147018
inflacja_październik_2023 = 1.16573339872354
inflacja_listopad_2023 = -0.404186717638335
inflacja_grudzień_2023 = 1.4997085208312
kwota_styczeń_2022 = (1 + ((inflacja_styczeń_2022 + 3)/1200)) * kwota_początkowa - 200
kwota_luty_2022 = (1 + ((inflacja_luty_2022 + 3)/1200)) * kwota_styczeń_2022 - 200
kwota_marzec_2022 =(1 + ((inflacja_marzec_2022 + 3)/1200)) * kwota_luty_2022 - 200
kwota_kwiecień_2022 = (1 + ((inflacja_kwiecień_2022 + 3)/1200)) * kwota_marzec_2022 - 200
kwota_maj_2022 = (1 + ((inflacja_maj_2022 + 3)/1200)) * kwota_kwiecień_2022 - 200
kwota_czerwiec_2022 = (1 + ((inflacja_czerwiec_2022 + 3)/1200)) * kwota_maj_2022 - 200
kwota_lipiec_2022 = (1 + ((inflacja_lipiec_2022 + 3)/1200)) * kwota_czerwiec_2022 - 200
kwota_sierpień_2022 = (1 + ((inflacja_sierpień_2022 + 3)/1200)) * kwota_lipiec_2022 - 200
kwota_wrzesień_2022 = (1 + ((inflacja_wrzesień_2022 + 3)/1200)) * kwota_sierpień_2022 - 200
kwota_październik_2022 = (1 + ((inflacja_październik_2022 + 3)/1200)) * kwota_wrzesień_2022 - 200
kwota_listopad_2022 = (1 + ((inflacja_listopad_2022 + 3)/1200)) * kwota_październik_2022 - 200
kwota_grudzień_2022 = (1 + ((inflacja_grudzień_2022 + 3)/1200)) * kwota_listopad_2022 - 200
kwota_styczeń_2023 = (1 + ((inflacja_styczeń_2023 + 3)/1200)) * kwota_grudzień_2022 - 200
kwota_luty_2023 = (1 + ((inflacja_luty_2023 + 3)/1200)) * kwota_styczeń_2023 - 200
kwota_marzec_2023 = (1 + ((inflacja_marzec_2023 + 3)/1200)) * kwota_luty_2023 - 200
kwota_kwiecień_2023 = (1 + ((inflacja_kwiecień_2023 + 3)/1200)) * kwota_marzec_2023 - 200
kwota_maj_2023 = (1 + ((inflacja_maj_2023 + 3)/1200)) * kwota_kwiecień_2023 - 200
kwota_czerwiec_2023 = (1 + ((inflacja_czerwiec_2023 + 3)/1200)) * kwota_maj_2023 - 200
kwota_lipiec_2023 = (1 + ((inflacja_lipiec_2023 + 3)/1200)) * kwota_czerwiec_2023 - 200
kwota_sierpień_2023 = (1 + ((inflacja_sierpień_2023 + 3)/1200)) * kwota_lipiec_2023 - 200
kwota_wrzesień_2023 = (1 + ((inflacja_wrzesień_2023 + 3)/1200)) * kwota_sierpień_2023 - 200
kwota_październik_2023 = (1 + ((inflacja_październik_2023 + 3)/1200)) * kwota_wrzesień_2023 - 200
kwota_listopad_2023 = (1 + ((inflacja_listopad_2023 + 3)/1200)) * kwota_październik_2023 - 200
kwota_grudzień_2023 = (1 + ((inflacja_grudzień_2023 + 3)/1200)) * kwota_listopad_2023 - 200
print(f'Twoja pozostała kwota kredytu to:" {kwota_styczeń_2022}, "to {kwota_początkowa - kwota_styczeń_2022} mniej niż w poprzednim miesiącu.')
print(f'Twoja pozostała kwota kredytu to:" {kwota_luty_2022}, "to {kwota_styczeń_2022 - kwota_luty_2022} mniej niż w poprzednim miesiącu.')
print(f'Twoja pozostała kwota kredytu to:" {kwota_marzec_2022}, "to {kwota_luty_2022 - kwota_marzec_2022} mniej niż w poprzednim miesiącu.')
print(f'Twoja pozostała kwota kredytu to:" {kwota_kwiecień_2022}, "to {kwota_marzec_2022 - kwota_kwiecień_2022} mniej niż w poprzednim miesiącu.')
print(f'Twoja pozostała kwota kredytu to:" {kwota_maj_2022}, "to {kwota_kwiecień_2022 - kwota_maj_2022} mniej niż w poprzednim miesiącu.')
