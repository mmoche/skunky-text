def calculator(options_dict):
    high_score_count = 0

# don't calculate a max value if the options dictionary is empty, otherwise calculate max value
    if not options_dict:
        pass
    else:
        high_score = max(options_dict.values())

# iterate through options based on # of max values and issue a recommendation
    for key in options_dict:
        score = options_dict.get(key)
        if score == high_score:
            high_score_count += 1
# where there is no high score, send a generic response
    if high_score_count == 0:
        print "Looks like we don't have a good option. Call the help line for more assistance."
# where there are multiple high scores, display all high score options
    elif high_score_count > 1:
        if len(options_dict.values()) != len(set(options_dict.values())):
            print "There's more than one suitable option: "
            max_value = max(options_dict.values())
            # print "Max: ", max_value
            for key in options_dict:
                get_value = options_dict.get(key)
                # print get_value
                if get_value == max_value:
                    print key, get_value
# where there's only one high score, display that option and expose the options that lost out
    elif high_score_count == 1:
        venue = max(options_dict, key=options_dict.get)
        print "Your best option is", venue
        print "Here's how each of our options stack up: "
        for choice, scored_choice in options_dict:
            print choice, "marcus", scored_choice
# generic error if the above statements are ambiguous
    else:
        print "Something's gone wrong"
