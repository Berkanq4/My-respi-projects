go = True
go2 = True
go3 = True
alph = ['a','b','c','d','e','f','g','h']
nums = ['1','2','3','4','5','6','7','8']
horizontal_knight = input("Please enter horizontal position of the knight (a,b,c,d,e,f,g,h): ").lower()

if (horizontal_knight.isalpha()):
    if (len(horizontal_knight) < 2):
       if(horizontal_knight in alph):
           horknight = alph.index(horizontal_knight)
           vertical_knight = (input("Please enter vertical position of the knight (1,2,3,4,5,6,7,8): "))
           if (vertical_knight.isdigit()):
               if (vertical_knight in nums):
                   verknight = nums.index(vertical_knight)
                   horizontal_bishop = input("Please enter horizontal position of the bishop (a,b,c,d,e,f,g,h): ").lower()
                   if (horizontal_bishop.isalpha()):
                       if (len(horizontal_bishop) < 2):
                           if (horizontal_bishop in alph):

                                horbishop = alph.index(horizontal_bishop)
                                vertical_bishop = input("Please enter vertical position of the bishop (1,2,3,4,5,6,7,8): ")
                                if (vertical_bishop.isdigit()):
                                   if (int(vertical_bishop) <= 8 and int(vertical_bishop) >= 1):
                                       verbishop = nums.index(vertical_bishop)
                                       atin_hareketi = []
                                       devam = True

                                       if (horknight <= 5 and verknight <= 6):
                                           possible_horizontal2 = horknight + 2
                                           possible_vertical1 = verknight + 1
                                           move1 = alph[possible_horizontal2] + nums[possible_vertical1]
                                           atin_hareketi.append(move1)

                                       if (horknight <= 6 and verknight <= 5):
                                           possible_horizontal1 = horknight + 1
                                           possible_vertical2 = verknight + 2
                                           move2 = alph[possible_horizontal1] + nums[possible_vertical2]
                                           atin_hareketi.append(move2)

                                       if (1 <= horknight and 2 <= verknight):
                                           possible_horizontalx = horknight - 1
                                           possible_verticalx = verknight - 2
                                           move3 = alph[possible_horizontalx] + nums[possible_verticalx]
                                           atin_hareketi.append(move3)

                                       if (2 <= horknight and 1 <= verknight):
                                           possible_horizontalx2 = horknight - 2
                                           possible_verticalx2 = verknight - 1
                                           move4 = alph[possible_horizontalx2] + nums[possible_verticalx2]
                                           atin_hareketi.append(move4)

                                       if (2 <= horknight and verknight <= 6):
                                           mumkun_dusey = horknight - 2
                                           mumkun_yatay = verknight + 1
                                           move5 = alph[mumkun_dusey] + nums[mumkun_yatay]
                                           atin_hareketi.append(move5)

                                       if (1 <= horknight and verknight <= 5):
                                           mumkun_dusey2 = horknight - 1
                                           mumkun_yatay2 = verknight + 2
                                           move6 = alph[mumkun_dusey2] + nums[mumkun_yatay2]
                                           atin_hareketi.append(move6)

                                       if (horknight <= 6 and 2 <= verknight):
                                           olanakli_dusey = horknight + 1
                                           olanakli_yatay = verknight - 2
                                           move7 = alph[olanakli_dusey] + nums[olanakli_yatay]
                                           atin_hareketi.append(move7)

                                       if (horknight <= 5 and 1 <= verknight):
                                           olanakli_dusey2 = horknight + 2
                                           olanakli_yatay2 = verknight - 1
                                           move8 = alph[olanakli_dusey2] + nums[olanakli_yatay2]
                                           atin_hareketi.append(move8)

                                       i = horbishop
                                       j = verbishop
                                       filin_hareketi = []
                                       baslangic = horizontal_bishop + vertical_bishop

                                       while (i <= 6 and i >= 0 and j <= 6 and j >= 0):
                                           i += 1
                                           j += 1
                                           zaa = alph[i] + nums[j]
                                           filin_hareketi.append(zaa)

                                       k = horbishop
                                       l = verbishop
                                       while (k <= 7 and k >= 1 and l <= 7 and l >= 1):
                                           k -= 1
                                           l -= 1
                                           yaa = alph[k] + nums[l]
                                           filin_hareketi.append(yaa)

                                       m = horbishop
                                       n = verbishop
                                       while (1 <= m and n <= 6):
                                           m -= 1
                                           n += 1
                                           maa = alph[m] + nums[n]
                                           filin_hareketi.append(maa)

                                       while (m <= 6 and 1 <= n):
                                           m += 1
                                           n -= 1
                                           naa = alph[m] + nums[n]
                                           filin_hareketi.append(naa)

                                       if (baslangic in filin_hareketi):
                                            filin_hareketi.remove(baslangic)

                                       filinkonumu = horizontal_bishop + vertical_bishop
                                       atinkonumu = horizontal_knight + vertical_knight

                                       devam = True
                                       if ((filinkonumu != atinkonumu)):
                                           if (filinkonumu in atin_hareketi):
                                               print("Knight can attack bishop")
                                               devam = False

                                           elif (atinkonumu in filin_hareketi):
                                               print("Bishop can attack knight")
                                               devam = False

                                       elif (filinkonumu == atinkonumu):
                                           print("They can't be in the same square")
                                           devam = False

                                       if (devam):
                                           print("Neither of them can attack each other")

                                   else:
                                       print("Vertical input for bishop is not a proper number")
                                else:
                                    print("Vertical input for bishop is not a number")
                           else:
                                print("Horizontal input for bishop is not a proper letter")
                       else:
                           print("Horizontal input for bishop is not a letter")
                   else:
                        print("Horizontal input for bishop is not a letter")
               else:
                   print("Vertical input for knight is not a proper number")
           else:
                print("Vertical input for knight is not a number")
       else:
            print("Horizontal input for knight is not a proper letter")
    else:
        print("Horizontal input for knight is not a letter")
else:
    print("Horizontal input for knight is not a letter")
