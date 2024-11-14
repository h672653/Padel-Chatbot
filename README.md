ML - Padel-Chatbot
Emir Bulduk, Sidar Baran 

BESKRIV PROBLEMET
SCOPE
Business Objective: Målet med prosjektet er å lage en chatbot som gir brukere svar på regler og spørsmål om padel. Chatboten skal gjøre det lettere for nye og erfarne spillere å forstå spillets regler uten å måtte søke på nettet eller lese lange regelbøker.
Hvordan brukes løsningen: Chatboten vil være tilgjengelig via en nettside eller app der brukerne kan stille spørsmål om padel-regler og få raske svar. I dag er denne informasjonen ofte tilgjengelig via nettsøk, men det kan være tungvint og tidkrevende. Uten maskinlæring kunne dette vært gjort manuelt ved å oppdatere en FAQ-side, men en chatbot gir en mer interaktiv og brukervennlig opplevelse.
Business Metrics: Ytelsen vil måles ved hvor nøyaktig og raskt chatboten svarer på brukerforespørsler. En suksessmetrik vil være hvor mange riktige svar chatboten gir i forhold til brukerforespørslene og brukertilfredshet (brukerfeedback).
Systembeskrivelse: Chatboten vil være en komponent i et enkelt spørre-svar-system basert på regler vi har samlet og strukturert i JSON-format, samt et Python-program som bruker maskinlæringsalgoritmer for å forstå spørsmål. Endringer i JSON-reglene eller algoritmer kan påvirke chatbotens ytelse.
Stakeholders: Brukere av padel-chatboten (padelspillere og trenere), utviklingsteamet (oss), og eventuelle fremtidige partnere som vil distribuere eller bruke chatboten.
Tentativ Tidslinje:
Uke 1-2: Datainnsamling og strukturering av regler
Uke 3-4: Utvikling av prototype og testing
Uke 5: Feilsøking og optimalisering
Uke 6: Lansering og innsamling av brukertilbakemeldinger
Ressurser: Vi trenger en server eller skytjeneste for å hoste chatboten, samt utviklingsverktøy som Python og HTML for å bygge grensesnittet.

METRIKKER
Business Metric: Minimum 90 % nøyaktighet på riktige svar i forhold til alle spørsmål som stilles.
ML/Software Metrics:
Treffsikkerhet (Accuracy) for riktig identifikasjon av spørsmål og svar, helst over 90 %.
Latency: Målet er en responstid under 2 sekunder for hvert spørsmål.
Throughput: Antall forespørsler chatboten kan håndtere per minutt.

DATA
Datakilder og Labels: Dataene består av padel-regler og vanlige spørsmål samlet i et JSON-datasett. Vi har samlet og manuelt verifisert spørsmål og svar for å sikre konsistens. Foreløpig har vi nok data for å trene en basisversjon av chatboten, men vi kan trenge ytterligere data om brukernes spørsmål for videre forbedring.
Etiske hensyn: Ingen sensitive eller personlige data er involvert. Vi holder oss kun til offentlige regler og allmenne spørsmål.
Dataprosessering: Vi bruker Python for å rense og strukturere data. Innholdet fra JSON-filen må konverteres til et format chatboten kan tolke effektivt. Funksjoner som spørsmålskategorisering og nøkkelordhåndtering vil bli vurdert for å forbedre nøyaktigheten.

MODELLERING
Modellvalg: Vi starter med en enkel beslutningstre-modell eller en regelbasert modell basert på nøkkelord. Hvis dette ikke gir tilstrekkelig nøyaktighet, kan vi eksperimentere med en dypere, maskinlæringsbasert NLP-modell.
Baseline-ytelse: Vi estimerer baseline med enkle nøkkelordsøk og matcher direkte med forhåndsdefinerte svar.
Feilprediksjoner: Ved feil i svarene vil vi analysere spørsmål for å forbedre modellens evne til å tolke ulike måter brukere formulerer spørsmål på.

DEPLOYMENT
Produksjonsoppsett: Chatboten vil bli driftet på en nettside eller app hvor brukere kan stille spørsmål. Vi vil monitorere ytelse og samle inn brukertilbakemeldinger for å sikre at systemet fungerer godt over tid.
Monitorering og Vedlikehold: Jevnlig testing av spørre-svar-funksjonalitet og justering av modellen basert på nye spørsmål fra brukerne. Vi vil også oppdatere regelsettet etter behov for å sikre at chatboten holder seg relevant.

REFERANSER

Regler for Padel   Inter Padel
https://interpadel.no/hva-er-padel/padel-spilleregler/
