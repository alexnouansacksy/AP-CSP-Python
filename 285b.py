from Cl285b import Salesperson

def main():
    try:
        print("Number   Code   Sales   Commission")
        people = []
        with open("data/prog285b.txt", 'r') as f:
            for line in f:
                ldata = line.split(" ")
                id = int(ldata[0])
                code = int(ldata[1])
                sales = float(ldata[2])
                dude = Salesperson(id, code, sales)
                people.append(dude)
        for sp in people:
            sp.calc()
            print(sp)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()

'''
Number   Code   Sales   Commission
101   17  $2250.0   $213.75
103   5   $4000.0   $300.00
117   3   $7350.0   $0.00
118   8   $7350.0   $574.75
125   5   $6500.0   $502.50
138   17  $6375.0   $677.50
192   8   $8125.0   $640.62
203   8   $3250.0   $243.75
218   5   $5000.0   $375.00
235   5   $5250.0   $396.25
264   17  $4150.0   $410.50
291   17  $750.0   $71.25

Process finished with exit code 0
'''