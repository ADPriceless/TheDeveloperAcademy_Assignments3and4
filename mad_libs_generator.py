def make_story():
    name = input('What is thingy\'s name again? ')
    job = input('That\'s right... And what is their job again? ')
    work_life = input('Oh, of course! What do they think about that? ')

    print(f'I bet {name} has some crazy stories...')

    thing = input('Wasn\'t there that one about the, um, you know, the... ')
    object_ = input('Right! And it appeared from the... ')
    verb = input('... then it ')

    animal = input('Wasn\'t there that other one with that animal? What was it again? a... ')
    print('Gosh! Now that one was wild!')
    defence = input(f'I\'m glad the {animal} was afraid of... ')
    print('Otherwise that would have been a disaster!')
    summary = input('If I had to sum it up in one word, I\'d say... ')
    print('Exactly!\n')

    story = f"{name} is a {job}. {name}'s job as a {job} is very {work_life}." + \
    f"\nOne day, while working, a {thing} burst in through the {object_}" + \
    f" and {verb}! How crazy!" + \
    f"\n\nBut the craziest one of all was when the {animal} escaped from the zoo!" + \
    f" And all poor {name} had to catch it with was the {defence}. Then, when the {thing} came" + \
    f" back the whole thing went {summary}."

    print(story)


if __name__ == '__main__':
    make_story()
