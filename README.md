## Pytania
1. Wpływ lokalizacji uczelni na zarobki i
zatrudnienie absolwentów, badając, czy różnice regionalne oraz prestiż uczelni mają znaczenie dla kariery
zawodowej

2. Jak zdobyte podczas studiów
doświadczenie zawodowe wpływa na wynagrodzenia i czas znalezienia pracy

3. Czy potencjalne zarobki wpływają na wybór kierunku studiów przez studentów

4. Czy poziom studiów (I vs II i JM) wpływa na przyszłe zarobki

5. Czy  forma studiów (studia dzienne vs zaoczne)
wpływa na przyszłe zarobki

## Model
W ramach projektu zostanie utworzony model, który posłuży do prognozowania przyszłych zarobków
absolwentów na podstawie wybranej dziedziny kształcenia studiów (domyślnie informatyka). 

## Wykresy

1. **f(P_WOJ) = (P_ME_ZAR lub P_WWZ)  i P_WWB**

    **P_WOJ** - Województwo lokalizacji jednostki dydaktycznej = P_ME_ZAR i P_WWB

    **P_ME_ZAR** - Mediana średnich miesięcznych wynagrodzeń absolwentów ze wszystkich źródeł po uzyskaniu dyplomu

    **P_WWZ** - Względny Wskaźnik Zarobków absolwentów po uzyskaniu dyplomu
    
    **P_WWB** - Względny Wskaźnik Bezrobocia absolwentów po uzyskaniu dyplomu

2. **f() = ?**

    **P_WWB_DOSW** - Względny Wskaźnik Bezrobocia absolwentów po uzyskaniu dyplomu wśród absolwentów z doświadczeniem pracy przed uzyskaniem dyplomu

    **P_WWB_NDOSW** - Względny Wskaźnik Bezrobocia absolwentów po uzyskaniu dyplomu wśród absolwentów bez doświadczenia pracy przed uzyskaniem dyplomu

    **P_CZAS_PRACA_DOSW** - Średni czas (w miesiącach) od uzyskania dyplomu do podjęcia pierwszej pracy po uzyskaniu dyplomu wśród absolwentów z doświadczeniem pracy przed uzyskaniem dyplomu

     **P_CZAS_PRACA_NDOSW** - Średni czas (w miesiącach) od uzyskania dyplomu do podjęcia pierwszej pracy po uzyskaniu dyplomu wśród absolwentów bez doświadczenia pracy przed uzyskaniem dyplomu

    **P_ME_ZAR_DOSW** - Mediana średnich miesięcznych wynagrodzeń ze wszystkich źródeł po uzyskaniu dyplomu absolwentów wśród absolwentów z doświadczeniem pracy przed uzyskaniem dyplomu

     **P_ME_ZAR_NDOSW** - Mediana średnich miesięcznych wynagrodzeń ze wszystkich źródeł po uzyskaniu dyplomu absolwentów wśród absolwentów bez doświadczenia pracy przed uzyskaniem dyplomu

    ### Dodatkowo 
     **f(Lata 1-5) = (P_WWZ_DOSW_PX i P_WWZ_NDOSW_PX) i (P_ME_ZAR_DOSW_PX i P_ME_ZAR_NDOSW_PX)**

     **P_ME_ZAR_DOSW** - Mediana średnich miesięcznych wynagrodzeń ze wszystkich źródeł po uzyskaniu dyplomu absolwentów wśród absolwentów z doświadczeniem pracy przed uzyskaniem dyplomu

     **P_ME_ZAR_NDOSW** - Mediana średnich miesięcznych wynagrodzeń ze wszystkich źródeł po uzyskaniu dyplomu absolwentów wśród absolwentów bez doświadczenia pracy przed uzyskaniem dyplomu

     **P_ME_ZAR_DOSW_PX** - Mediana średnich miesięcznych wynagrodzeń ze wszystkich źródeł w X roku po uzyskaniu dyplomu absolwentów wśród absolwentów z doświadczeniem pracy przed uzyskaniem dyplomu

     **P_ME_ZAR_NDOSW_PX** - Mediana średnich miesięcznych wynagrodzeń ze wszystkich źródeł w X roku po uzyskaniu dyplomu absolwentów wśród absolwentów bez doświadczenia pracy przed uzyskaniem dyplomu

3. **Histogram - f(P_N) = P_ME_ZAR**

    **P_N** - Liczba studentów (z tabeli students-major-data.csv)

    **P_ME_ZAR** - Mediana średnich miesięcznych wynagrodzeń absolwentów ze wszystkich źródeł po uzyskaniu dyplomu

4. **f(P_POZIOM) = (P_ME_ZAR lub P_WWZ)**

    **P_POZIOM** - Stopień ukończonych studiów

    **P_WOJ** - Województwo lokalizacji jednostki dydaktycznej = P_ME_ZAR i P_WWB

    **P_ME_ZAR** - Mediana średnich miesięcznych wynagrodzeń absolwentów ze wszystkich źródeł po uzyskaniu dyplomu

5. **f(P_FORMA) = (P_ME_ZAR lub P_WWZ)**

    **P_FORMA** - Forma ukończonych studiów

    **P_WOJ** - Województwo lokalizacji jednostki dydaktycznej = P_ME_ZAR i P_WWB

    **P_ME_ZAR** - Mediana średnich miesięcznych wynagrodzeń absolwentów ze wszystkich źródeł po uzyskaniu dyplomu

## Dodatkowe wykresy
1. **f(Miesiące X 1-60) = P_WWZ_MIES_X i P_WWB_MIES_X**

    **P_WWZ_MIES_X** - Względny Wskaźnik Zarobków w X. miesiącu po uzyskaniu dyplomu

    **P_WWB_MIES_X** - Względny Wskaźnik Bezrobocia w X. miesiącu po uzyskaniu dyplomu