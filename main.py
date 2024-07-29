import streamlit as st
import random


# Mockup data for the quiz

answers = ["Nooit", "Soms", "Vaak"]

questions = {
    0: "Ik heb meegedaan aan online pesten of cyberpesten.",
    1: "Ik heb een foto of video van iemand gedeeld zonder hun toestemming.",
    2: "Ik heb meegedaan aan het verspreiden van roddels over iemand.",
    3: "Ik heb iemand geforceerd om iets te doen wat ze niet wilden (zoals spijbelen, stelen, etc.).",
    4: "Ik heb een ander uitgescholden of beledigd via sociale media.",
    5: "Ik heb meegedaan aan het belachelijk maken van iemand in de groep.",
    6: "Ik heb iemand gevraagd om naaktfoto's te sturen.",
    7: "Ik heb geprobeerd iemand te kussen zonder eerst hun toestemming te vragen.",
    8: "Ik heb ooit iemand geslagen of fysiek pijn gedaan tijdens een ruzie.",
    9: "Ik heb weleens aan anderen verteld dat ik hen zou slaan of pijn doen als ze iets deden wat ik niet wilde.",
}

def main():
    st.title("GGG Quiz")

    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.user_answers = {}

    current_question = st.session_state.current_question
    score = st.session_state.score

    if current_question < len(questions):
        q = questions[current_question]
        if current_question not in st.session_state.user_answers:
            default = None
        else:
            default = st.session_state.user_answers[current_question]
            if default is not None:
                default = answers.index(default)

        user_answer = st.radio(
            f"Vraag {current_question + 1}: {questions[current_question]}",
            answers,
            index=default,
            key=f"q{current_question}"
        )
        
        if current_question < len(questions) - 1:
            next_string = "Volgende"
        else:
            next_string = "Dien in"

        col1, col2 = st.columns([1,1])

        with col1:
            if current_question > 0 and st.button("Vorige"):
                st.session_state.user_answers[current_question] = user_answer
                print(st.session_state.user_answers)
                st.session_state.current_question -= 1
                st.experimental_rerun()
        with col2:
            if st.button(next_string):
                st.session_state.user_answers[current_question] = user_answer
                print(st.session_state.user_answers)
                st.session_state.current_question += 1
                st.experimental_rerun()


    else:
        st.subheader("Resultaten:")

        user_answers_list = list(st.session_state.user_answers.values())
        nooit_count = user_answers_list.count('Nooit')
        soms_count = user_answers_list.count('Soms')
        vaak_count = user_answers_list.count('Vaak')

        score = vaak_count * 3 + soms_count

        if score < 3:
            st.markdown("""
Je bent iemand die veel aandacht besteedt aan de wensen en grenzen van anderen en je doet echt je best om die te respecteren. Als je twijfelt of iemand zich op zijn gemak voelt, aarzel je niet om het rechtstreeks te vragen. Je zorgt ervoor dat je duidelijk communiceert en checkt of alles goed is, zodat iedereen zich gewaardeerd en comfortabel voelt. Deze zorgvuldige aanpak helpt om een vriendelijke en respectvolle sfeer te creëren, en dat maakt een groot verschil in hoe anderen zich bij jou voelen.

Heb je ooit zelf ervaring gehad met grensoverschrijdend gedrag, of het nu bij jezelf of bij anderen is? Bezoek de volgende websites voor meer informatie en ondersteuning:

**Websites**

1.  (cyber)pesten:
    
    -   [Allesoverpesten.be(dit is een externe link)](http://www.allesoverpesten.be/)
        
2.  seksueel grensoverschrijdend gedrag:
    
    -   [Sensoa.be - tips, tools en handvatten rond relationele en seksuele vorming, seksuele gezondheid, seksueel grensoverschrijdend gedrag en misbruik(dit is een externe link)](https://www.sensoa.be/)
        

Heb je nog vragen, wil je een melding doen, of je verhaal delen? Dit kan op de volgende plekken:

-   [Bel 0800 13 184 over grensoverschrijdend gedrag](https://www.vlaanderen.be/vlaams-meldpunt-grensoverschrijdend-gedrag/telefoneer-ons-over-grensoverschrijdend-gedrag)
    
-   [Chat over grensoverschrijdend gedrag](https://www.vlaanderen.be/vlaams-meldpunt-grensoverschrijdend-gedrag/chat-met-ons-over-grensoverschrijdend-gedrag)
    
-   [Mail over grensoverschrijdend gedrag naar meldpunt@vlaanderen.be](mailto:Mail%20over%20grensoverschrijdend%20gedrag%20naar%20meldpunt@vlaanderen.be)
    
-   [Watwat.be - no-nonsense info voor jongeren(dit is een externe link)](https://www.watwat.be/)
    
-   [https://www.caw.be/jac/](https://www.caw.be/jac/)
    
-   [https://awel.be/themas/wat-grensoverschrijdend-gedrag](https://awel.be/themas/wat-grensoverschrijdend-gedrag)
            """)


        else:
            st.markdown("""
Het lijkt erop dat je soms worstelt met het respecteren van de wensen en grenzen van anderen. Onthoud dat jouw gedrag invloed heeft op anderen. Het is daarom belangrijk om altijd eerst toestemming te vragen en respectvol te zijn. Check of de ander het oké vindt wat je doet of zegt. Je kunt dat gewoon vragen en zo zorgen voor een veilige en fijne omgeving voor iedereen.

**Tips voor het respecteren van grenzen:**

1.  **Vraag altijd toestemming**:
    
    -   Voordat je iemand aanraakt, een opmerking maakt of een handeling voorstelt, vraag of het oké is.
        
    -   Bijvoorbeeld: "Is het goed als ik je een knuffel geef?" of "Vind je het oké als we hierover praten?"
        
2.  **Let op non-verbale signalementen**:
    
    -   Let op lichaamstaal en gezichtsuitdrukkingen. Als iemand zich ongemakkelijk of terughoudend lijkt te voelen, stop dan en vraag hoe ze zich voelen.
        
    -   Bijvoorbeeld: Als iemand wegkijkt, zich terugtrekt of stil wordt, kan dat een teken zijn dat ze zich niet op hun gemak voelen.
        
3.  **Wees duidelijk en direct**:
    
    -   Als je niet zeker weet of iets gepast is, vraag het direct en respecteer het antwoord, ongeacht wat je hoopt te horen.
        
    -   Bijvoorbeeld: "Vind je het oké als ik hierover praat?" of "Wil je dit graag doen?"
        
4.  **Respecteer "Nee" en grenzen**:
    
    -   Als iemand "nee" zegt of een grens stelt, respecteer dat zonder te pushen of te proberen hen van gedachten te doen veranderen.
        
    -   Bijvoorbeeld: "Ik begrijp het, geen probleem" of "Bedankt dat je het zegt, laten we iets anders doen."
        
5.  **Communiceer openlijk**:
    
    -   Moedig open communicatie aan over wat wel en niet comfortabel is voor beide partijen.
        
    -   Bijvoorbeeld: "Hoe voel je je hierbij?" of "Laat me weten als iets je ongemakkelijk maakt."
        
6.  **Reflecteer op je gedrag**:
    
    -   Denk na over je eigen acties en hoe deze anderen kunnen beïnvloeden. Vraag jezelf af of je respectvol en empathisch handelt.
        
    -   Bijvoorbeeld: "Zou ik me hier comfortabel bij voelen als ik in hun schoenen stond?"
        
7.  **Wees empathisch**:
    
    -   Probeer te begrijpen hoe de ander zich voelt en toon medeleven. Dit helpt om een veilige en respectvolle omgeving te creëren.
        
    -   Bijvoorbeeld: "Ik begrijp dat je je zo voelt, wat kan ik doen om te helpen?"
        
8.  **Leer en groei**:
    
    -   Informeer jezelf over wat gepast gedrag is en leer van je fouten. Iedereen maakt fouten, maar het is belangrijk om te leren en te verbeteren.
        
    -   Bijvoorbeeld: "Ik realiseer me dat mijn gedrag verkeerd was, het spijt me en ik zal eraan werken om beter te doen."
        
9.  **Zoek hulp als dat nodig is**:
    
    -   Als je merkt dat je moeite hebt om grenzen te respecteren of als je zelf slachtoffer bent van grensoverschrijdend gedrag, zoek hulp bij een vertrouwenspersoon, leraar, ouder of een professionele hulpverlener.
        
    -   Bijvoorbeeld: "Ik heb hulp nodig om beter om te gaan met mijn gedrag" of "Ik heb dit meegemaakt en ik heb ondersteuning nodig."
        

  

Als je jong bent en merkt dat je soms dingen doet die niet helemaal goed voelen, kun je op deze websites terecht voor hulp en advies:

**Websites**

-   [https://www.allesoverpesten.be/vragen/hoe-stop-ik-zelf-met-pesten](https://www.allesoverpesten.be/vragen/hoe-stop-ik-zelf-met-pesten)

-   [Sensoa.be - tips, tools en handvatten rond relationele en seksuele vorming, seksuele gezondheid, seksueel grensoverschrijdend gedrag en misbruik(dit is een externe link)](https://www.sensoa.be/)
    
-   [www.kindermishandeling.be](http://www.kindermishandeling.be/)
    

Heb je nog vragen, wil je een melding doen, of je verhaal delen? Dit kan op de volgende plekken:

-   [Bel 0800 13 184 over grensoverschrijdend gedrag](https://www.vlaanderen.be/vlaams-meldpunt-grensoverschrijdend-gedrag/telefoneer-ons-over-grensoverschrijdend-gedrag)
    
-   [Chat over grensoverschrijdend gedrag](https://www.vlaanderen.be/vlaams-meldpunt-grensoverschrijdend-gedrag/chat-met-ons-over-grensoverschrijdend-gedrag)
    
-   [Mail over grensoverschrijdend gedrag naar meldpunt@vlaanderen.be](mailto:Mail%20over%20grensoverschrijdend%20gedrag%20naar%20meldpunt@vlaanderen.be)
    
-   [Watwat.be - no-nonsense info voor jongeren(dit is een externe link)](https://www.watwat.be/)
    
-   [https://www.caw.be/jac/](https://www.caw.be/jac/)
    
-   [https://awel.be/themas/wat-grensoverschrijdend-gedrag](https://awel.be/themas/wat-grensoverschrijdend-gedrag)
            """)

if __name__ == "__main__":
    main()