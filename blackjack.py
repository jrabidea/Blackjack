from random import *

print "*********************************"
print "           BLACKJACK             "
print "*********************************"


players_hand = []
dealers_hand = []
discard_pile = []

card_deck = {
	
	"Ad" : 1,
	"2d" : 2,
	"3d" : 3,
	"4d" : 4,
	"5d" : 5,
	"6d" : 6,
	"7d" : 7,
	"8d" : 8,
	"9d" : 9,
	"10d" : 10,
	"Jd" : 10,
	"Qd" : 10,
	"Kd" : 10,
	"As" : 1,
	"2s" : 2,
	"3s" : 3,
	"4s" : 4,
	"5s" : 5,
	"6s" : 6,
	"7s" : 7,
	"8s" : 8,
	"9s" : 9,
	"10s" : 10,
	"Js" : 10,
	"Qs" : 10,
	"Ks" : 10,
	"Ac" : 1,
	"2c" : 2,
	"3c" : 3,
	"4c" : 4, 
	"5c" : 5, 
	"6c" : 6, 
	"7c" : 7, 
	"8c" : 8, 
	"9c" : 9, 
	"10c" : 10, 
	"Jc" : 10, 
	"Qc" : 10, 
	"Kc" : 10,
	"Ah" : 1, 
	"2h" : 2, 
	"3h" : 3, 
	"4h" : 4, 
	"5h" : 5, 
	"6h" : 6,
	"7h" : 7, 
	"8h" : 8, 
	"9h" : 9, 
	"10h" : 10, 
	"Jh" : 10, 
	"Qh" : 10, 
	"Kh" : 10
}

suite = ["s", "c", "h", "d"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rand_num_card = randrange(0, 10, 1)
rand_num_suite = randrange(0, 4, 1)

print str(numbers[rand_num_card]) + suite[rand_num_suite]
