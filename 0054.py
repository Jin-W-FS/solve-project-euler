
class Poker:
    Order = '23456789TJQKA'
    def __init__(self, s):
        self.s = s
        self.t = s[0]
        self.n = Poker.Order.index(s[0])
        self.c = s[1]
    def __lt__(self, other):
        return self.n < other.n
    def __eq__(self, other):
        return self.n == other.n
    def __repr__(self):
        return 'Poker({})'.format(repr(self.s))


class ScoreKinds:
    (RoyalFlush, StraightFlush, FourOfAKind, FullHouse,
     Flush, Straight, ThreeOfAKind, TwoPairs, OnePair,
     HighCard) = range(10)
    NAMES = ('RoyalFlush', 'StraightFlush', 'FourOfAKind', 'FullHouse',
             'Flush', 'Straight', 'ThreeOfAKind', 'TwoPairs', 'OnePair',
             'HighCard')
    COUNT = 10


class PokerHand:
    @staticmethod
    def fromString(s):
        return PokerHand(Poker(ss) for ss in s.split())
    
    def __init__(self, pokes):
        self.pokes = tuple(sorted(pokes, reverse=True))
        self.types = [()] * ScoreKinds.COUNT
        self.analyse()

    def __str__(self):
        s = []
        for i in range(ScoreKinds.COUNT):
            if self.types[i]:
                s.append('{}: {};'.format(ScoreKinds.NAMES[i], self.types[i]))
        return '\t'.join(s)

    def __lt__(self, other):
        return self.types < other.types

    def __gt__(self, other):
        return self.types > other.types

    def checkStraight(self):
        for i in range(1, 5):
            if self.pokes[i].n != self.pokes[0].n - i:
                return False
        return True

    def checkFlush(self):
        for i in range(1, 5):
            if self.pokes[i].c != self.pokes[0].c:
                return False
        return True

    def checkSameKind(self):
        d = {}
        for p in self.pokes:
            if p.n in d:
                d[p.n].append(p)
            else:
                d[p.n] = [p]
        l = [ (len(v), tuple(v)) for v in d.values() ]
        l.sort(reverse=True)
        return l

    def analyse(self):
        if self.checkStraight():
            if self.checkFlush():
                if self.pokes[0].t == 'A':
                    self.types[ScoreKinds.RoyalFlush] = self.pokes
                else:
                    self.types[ScoreKinds.StraightFlush] = self.pokes
            else:
                self.types[ScoreKinds.Straight] = self.pokes
        elif self.checkFlush():
            self.types[ScoreKinds.Flush] = self.pokes
        else:
            kinds = self.checkSameKind()
            if kinds[0][0] == 4:
                self.types[ScoreKinds.FourOfAKind] = kinds[0][1]
                self.types[ScoreKinds.HighCard] = kinds[1][1]
            elif kinds[0][0] == 3:
                if kinds[1][0] == 2:
                    self.types[ScoreKinds.FullHouse] = (kinds[0][1], kinds[1][1])
                else:
                    self.types[ScoreKinds.ThreeOfAKind] = kinds[0][1]
                    self.types[ScoreKinds.HighCard] = tuple(kinds[i][1][0] for i in range(1, 3))
            elif kinds[0][0] == 2:
                if kinds[1][0] == 2:
                    self.types[ScoreKinds.TwoPairs] = (kinds[0][1], kinds[1][1])
                    self.types[ScoreKinds.HighCard] = kinds[2][1]
                else:
                    self.types[ScoreKinds.OnePair] = kinds[0][1]
                    self.types[ScoreKinds.HighCard] = tuple(kinds[i][1][0] for i in range(1, 4))
            else:
                self.types[ScoreKinds.HighCard] = self.pokes


if __name__ == '__main__':
    cnt = 0
    for line in open('data/p054_poker.txt'):
        l, r = PokerHand.fromString(line[:15]), PokerHand.fromString(line[15:])
        if l > r:
            cnt += 1
        #    print(l, '> ', r)
        #else:
        #    print(l, '<=', r)
    print('\nTotal:', cnt)

        
