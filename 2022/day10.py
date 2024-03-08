def read_cathode_ray_instructions():
    with open('../resources/cathode_ray_instructions.txt') as instructions_file:
        instructions = instructions_file.read().splitlines()
