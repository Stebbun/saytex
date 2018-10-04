import sys
import os
import random

def is_balanced_square_parens(string):
    height = 0
    for c in string:
        if c == "[":
            height +=1
        elif c == "]":
            if height == 0:
                return False
            height -= 1
    return height == 0

def process_actor_line(actor, script, out_dir):
    if not is_balanced_square_parens(script):
        generate_actor_segment(actor, script, out_dir)
        return
    start_index = 0
    left_paren_index = script.find("[")
    while left_paren_index != -1:
        actor_part = script[start_index:left_paren_index]
        generate_actor_segment(actor, actor_part, out_dir)
        right_paren_index = script.find("]", left_paren_index) + 1
        narrator_part = script[left_paren_index:right_paren_index]
        generate_narrator_segment(narrator_part, out_dir)
        left_paren_index = left_paren_index = script.find("[", right_paren_index)
        start_index = right_paren_index
    actor_part = script[start_index:len(script)]
    generate_actor_segment(actor, actor_part, out_dir)

def generate_narrator_segment(script, out_dir):
    generate_actor_segment("Narrator", script, out_dir)

def generate_actor_segment(actor, script, out_dir):
    if len(script) == 0:
        return
    global segment_id
    filename = str(segment_id).zfill(5) + "_" + actor
    filename = os.path.join(out_dir, "sequences", filename)
    file = open(filename, "w")
    file.write(script)
    file.close()
    segment_id += 1

def process_line(line, out_dir, actors):
    line_arr = line.split(":", 1)
    if len(line_arr) == 1:
        #add narrator
        script = line_arr[0]
        generate_narrator_segment(script, out_dir)
    elif len(line_arr) == 2:
        #add actor
        actor = line_arr[0]
        script = line_arr[1]
        actors.add(actor)
        process_actor_line(actor, script, out_dir)

def parse(input_file, out_dir, actors):
    with open(input_file) as fp:
        os.mkdir(out_dir)
        os.mkdir(os.path.join(out_dir, "sequences"))
        for line in fp:
            process_line(line.strip(), out_dir, actors)

def generate_actor_voice_map(actors, out_dir):
    voice_file = open("voices", "r")
    voices = [line.split()[0].strip() for line in voice_file]
    map = dict([(actor, voices[random.randint(0, len(voices) - 1)]) for actor in actors])
    filename = "actor_voice_map"
    filename = os.path.join(out_dir, filename)
    file = open(filename, "w")
    for key, value in map.items():
        file.write(key + ":" + value + "\n")
    file.close()
    return map

def generate_command_sequence(out_dir, actor_voice_map):
    sequences = os.listdir(os.path.join(out_dir, "sequences"))
    sequences.sort()
    filename = os.path.join(out_dir, "command_sequence")
    seq_dir = os.path.join(out_dir, "sequences")
    file = open(filename, "w")
    for seq in sequences:
        seq_arr = seq.split("_")
        actor = seq_arr[1]
        voice = actor_voice_map[actor]
        file.write("say --voice=" + voice + " --input-file=" + os.path.join(seq_dir, seq) + "\n")
    file.close()

def main():
    input_file = sys.argv[1]
    out_dir = sys.argv[2]
    actors = set()
    actors.add("Narrator")
    parse(input_file, out_dir, actors)
    actor_voice_map = generate_actor_voice_map(actors, out_dir)
    generate_command_sequence(out_dir, actor_voice_map)
    #play_script(out_dir)

if __name__== "__main__":
    segment_id = 0
    main()
