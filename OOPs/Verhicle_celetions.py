import os


class Vehicles:
    def get_details_for_toyota(self,arg):
        try:
            self.bt = arg
            for each_items in self.bt.items():
                # return each_items
                return each_items
        except Exception as e:
            print(e)
        return None

    def get_details_for_mecerdes(self,data):
        try:
            self.nay = data
            for r,k in self.nay.items():
                print(f"Toyota details are",r)

            # for each_items in self.info.items():
            #     print(each_items)
        except Exception as e:
            print(e)
        return None


def main():
    try:
        Toyota = Vehicles()
        mecerdes = Vehicles()
        tesla = {'made': ['Camery', 'yorejr', 'uehej'],'Years_made': 19500, 'founded_by': 'fefeei'}
        roles_roles = {'made': ['Csdamry', 'yorjr', 'uehej'],'Years_made': 1940, 'founded_by': 'sdfdeea'}
        # Toyota.get_details_for_toyota({'made': ['Camry', 'yorjr', 'uehej'], 'Years_made': 1900, 'founded_by': 'Koji'})
        # print("-------------------")
        mecerdes.get_details_for_mecerdes({'made': ['Mecerdes', 'yorrjr', 'uehej'],'Years_made': 19803, 'founded_by': 'ujdjee'})
        'get_details_for_each_cars(Toyota)'
        'get_details_for_each_cars(Toyota)'
        # print(mecerdes.nay)
    except Exception as e:
        print(e)
    return None


if __name__ == '__main__':
        main()