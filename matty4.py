import calculator
import relevance_scores

# get input from user
condition = raw_input('Why do you need to see a doctor today?')

# define symptoms and scores per venue
er = {
    "cold":0.0665852808119527,
    "flu":0.0777831309001746,
    "allergies":0.088299593973934,
    "rash":0.0333478748199762,
    "cut":0.0870964219258614,
    "scrape":0.0793225998621539,
    "sprain":0.0877094768874901,
    "strain":0.0507824425253841,
    "strep":0.0590931529949941,
    "mono":0.0907405969410889,
    "pregnancy":0.0788924423783984,
    "physical":0.0783735048653762,
    "stitches":0.0424567589423496,
    "cough":0.0862927280769114,
    "chest":0.0720831965717249,
    "knee":0.0556833078297623,
    "ankle":0.0747736591917592,
    "wrist":0.0766786363646917,
    "pain":0.00891563858668005,
    "sleep":0.0279305445492268,
    "uti":0.0758338219314296,
    "pink":0.086829006153528,
    "eye":0.0010035746886324,
    "congestion":0.0787418483625296,
    "headache":0.0115438197003044,
    "migraine":0.054350884271325,
    "acne":0.0120367336839297,
    "nausea":0.0995471573377189,
    "heartburn":0.00437472825961671,
    "vomiting":0.0340038525951466,
    "diarrhea":0.0379625965160301,
    "infection":0.073064282907069,
    "back":0.0897918236431676,
    "burn":0.0602405001442079,
    "bite":0.0746169982816154,
    "sting":0.0339495183832217,
    "sore":0.0424568606806903,
    "toenail":0.0987347551469261,
    "measles":0.0549984967195832,
    "pox":0.0020288761251096,
    "emergency":1
}

ec = {
    "cold":0.067291344786254,
    "flu":0.0900958679007653,
    "allergies":0.0872535841778143,
    "rash":0.00145249241956993,
    "cut":0.00221644346880406,
    "scrape":0.0995163799544564,
    "sprain":0.099954749839121,
    "strain":0.0369101825390062,
    "strep":0.0673714065222104,
    "mono":0.0087719527520039,
    "pregnancy":0.0998312742422748,
    "physical":0.0534927771633636,
    "stitches":0.0761474612583319,
    "cough":0.012129610404326,
    "chest":0.0231367866368536,
    "knee":0.0783596173831088,
    "ankle":0.0887374000533847,
    "wrist":0.0763841645062979,
    "pain":0.0406133143971617,
    "sleep":0.096991230558305,
    "uti":0.0725617569587956,
    "pink":0.0909120880388562,
    "eye":0.0116959633401563,
    "congestion":0.0683016363287308,
    "headache":0.0206439374477727,
    "migraine":0.0166850721725878,
    "acne":0.0183618029847231,
    "nausea":0.0023531765094981,
    "heartburn":0.000548216659431988,
    "vomiting":0.0359918669254978,
    "diarrhea":0.0421304011054723,
    "infection":0.0268302181472493,
    "back":0.0747260185951889,
    "burn":0.0154310134301204,
    "bite":0.0871025551925012,
    "sting":0.0742537921347658,
    "sore":0.0315237230690407,
    "toenail":0.0533923007229386,
    "measles":0.00909343853502798,
    "pox":0.0480878737239814,
    "clinic":1
    }

virtual = {
    "cold":0.0240174368962579,
    "flu":0.0536639304689006,
    "allergies":0.0346736192805783,
    "rash":0.0970913813554296,
    "cut":0.082739973138859,
    "scrape":0.0814435254888669,
    "sprain":0.0618100949118121,
    "strain":0.000611530045424646,
    "strep":0.00675291561521686,
    "mono":0.0449747345149501,
    "pregnancy":0.035528128354424,
    "physical":0.0101243095156518,
    "stitches":0.0010192098349828,
    "cough":0.0360847892053715,
    "chest":0.0618404686524165,
    "knee":0.0405009421168509,
    "ankle":0.0602034833081892,
    "wrist":0.040639375845674,
    "pain":0.0379331705473162,
    "sleep":0.0515040227228157,
    "uti":0.0352775557861823,
    "pink":0.093027138408412,
    "eye":0.0170863536957584,
    "congestion":0.0891340252639747,
    "headache":0.0680131312272711,
    "migraine":0.000924352092107883,
    "acne":0.00276350377766705,
    "nausea":0.0539524516319992,
    "heartburn":0.0762506047266356,
    "vomiting":0.0027104438422058,
    "diarrhea":0.0590545548267798,
    "infection":0.0432466892572638,
    "back":0.0696278099932341,
    "burn":0.0683220922284596,
    "bite":0.0786292798900366,
    "sting":0.0112918574477924,
    "sore":0.0962921730148631,
    "toenail":0.00323713978192697,
    "measles":0.0173548487100257,
    "pox":0.0371271955741603,
    "virtual":1
}

athome = {
    "cold":0.0509827939063197,
    "flu":0.0489771447308281,
    "allergies":0.088870164543739,
    "rash":0.0412439325898039,
    "cut":0.013149271048558,
    "scrape":0.0864657680350102,
    "sprain":0.0394239329498852,
    "strain":0.0191664725136987,
    "strep":0.0496320899073852,
    "mono":0.0757121879971531,
    "pregnancy":0.0473914486871665,
    "physical":0.0796537221975034,
    "stitches":0.0442790512891133,
    "cough":0.0102424518959565,
    "chest":0.0861320732955669,
    "knee":0.0135799810955027,
    "ankle":0.0858296758174153,
    "wrist":0.0964409955433763,
    "pain":0.0569183614678488,
    "sleep":0.0909771963618415,
    "uti":0.0685572678248051,
    "pink":0.0472348025197851,
    "eye":0.0894994703306187,
    "congestion":0.0155519951459151,
    "headache":0.0553116275449308,
    "migraine":0.0424291834170956,
    "acne":0.0150202707617623,
    "nausea":0.0113222279086581,
    "heartburn":0.0961130997188575,
    "vomiting":0.023322392725864,
    "diarrhea":0.0177870290760968,
    "infection":0.0664273112043467,
    "back":0.0430380201186089,
    "burn":0.0875765006399275,
    "bite":0.0038639127645299,
    "sting":0.0323356221867711,
    "sore":0.0806176004355626,
    "toenail":0.0390343296551492,
    "measles":0.0641256256826918,
    "pox":0.0557387442922768,
    "home": 1
}

# calculate the relevance scores per venue
options = relevance_scores.relevance_scores(condition, er, ec, virtual, athome)

# call the relevance calculator module to identify best option
calculator.calculator(options)
