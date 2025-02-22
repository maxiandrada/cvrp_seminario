import sys

#Ejecutar de la forma: >> python cvrp.py input_file [output_file] [time_limit] [nb_trucks]

if __name__ == "__main__":
	if len(sys.argv) < 2:
        print ("Usage: python cvrp.py input_file [output_file] [time_limit] [nb_trucks]")
        sys.exit(1)

    instance_file = sys.argv[1]
    sol_file = sys.argv[2] if len(sys.argv) > 2 else None
    str_time_limit = sys.argv[3] if len(sys.argv) > 3 else "20"
    str_nb_trucks = sys.argv[4] if len(sys.argv) > 4 else "0"

    main(instance_file, str_time_limit, sol_file, str_nb_trucks)