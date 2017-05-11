def relevance_scores(user_input, er_venue, ec_venue, virtual_venue, at_home_venue):

    # initialize a bunch of variables
    er_score = 0
    er_relevant_words = 0
    ec_score = 0
    ec_relevant_words = 0
    virtual_score = 0
    virtual_relevant_words = 0
    athome_score = 0
    athome_relevant_words = 0
    total_relevant_words = 0
    options = {

    }
    er = er_venue
    ec = ec_venue
    virtual = virtual_venue
    athome = at_home_venue

    # take user input and split it into words
    all_words = user_input.split()
    # measure length of user input
    condition_words = len(all_words)
    # count relevant words and sum the scores of relevant words per venue
    for word in all_words:
        if word in er:
            er_score = er_score + er[word]
            er_relevant_words += 1
            total_relevant_words += 1

    for word in all_words:
        if word in ec:
            ec_score = ec_score + ec[word]
            ec_relevant_words += 1
            total_relevant_words += 1

    for word in all_words:
        if word in virtual:
            virtual_score = virtual_score + virtual[word]
            virtual_relevant_words += 1
            total_relevant_words += 1

    for word in all_words:
        if word in athome:
            athome_score = athome_score + athome[word]
            athome_relevant_words += 1
            total_relevant_words += 1

    # calculate relevance scores for venues whose relevance score > 0
    if er_score > 0:
        er_relevance = er_score*(float(er_relevant_words)/float(total_relevant_words))
        options["Emergency Room"] = er_relevance
    else:
        er_relevance = 0

    if ec_score > 0:
        ec_relevance = ec_score*(float(ec_relevant_words)/float(total_relevant_words))
        options["Express Care Clinic"] = ec_relevance
    else:
        ec_relevance = 0

    if virtual_score > 0:
        virtual_relevance = virtual_score*(float(virtual_relevant_words)/float(total_relevant_words))
        options["Express Care Virtual"] = virtual_relevance
    else:
        virtual_relevance = 0

    if athome_score > 0:
        athome_relevance = athome_score*(float(athome_relevant_words)/float(total_relevant_words))
        options["Express Care @ Home"] = athome_relevance
    else:
        athome_relevance = 0
    # send a dictionary of scored venues back to the app
    return options
