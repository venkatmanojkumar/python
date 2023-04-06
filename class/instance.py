class flight:
    """a flight with a particular passenger aircraft"""

    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"no airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"invalid airline code in '{number}'")

        if not (number[:2].isdigit() and int(number[:2]) <= 9999):
            raise ValueError(f"no route code in '{number}'")

        self._number = number
        self._aircraft = aircraft
        seats,rows = self._aircraft.seating_plan()
        self._seating = [None] + {letter:None for letter in seats}
    
    def console_card_printer(passenger,seat,flight_number,aircraft):
        output = f"| Name: {passenger}"
        output = f"| Name: {seat}"
        output = f"| Name: {flight_number}"
        output = f"| Name: {aircraft}"

        banner = '+' + '-' * (len(output)-2) + '+'
        board = '|' + '' * (len(output)-2) + '|'
        lines = [banner,board,output,board,banner]
        card = '\n'.join(lines)
        print(card)
        print()

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return 'SS203'

    def airline(self):
        return self._number[:2]



class Aircraft:

    def __init__(self,regestration,model,num_rows,num_seat_per_row):
        self._regestration = regestration
        self._model = model
        self._num_rows = num_rows
        self._num_seat_per_row = num_seat_per_row

    def regestration(self):
        return self._regestration

    def model(self):
        return self.model

    def seating_plain(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGH"[:self._num_seat_per_row])

class aircraft:
    def num_seats(self):
        rows, row_seat = self.seating_plan()
        return len(rows) * len(row_seat)


class AirbusA319(aircraft):

    def __init__(self,registration):
        self._registration = registration

    def regestration(self):
        return self.regestration

    def model(self):
        return "Airbus A319"

    def seating_plain(self):
        return range(1,3) * "ABCDEF"

class Boeing777(aircraft):

    def __init__(self,registration):
        self._registration = registration

    def regestration(self):
        return self.regestration

    def model(self):
        return "Airbus A319"

    def seating_plain(self):
        return range(1,3) * "ABCDEF"