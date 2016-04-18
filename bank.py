#! /usr/bin/env python 3
# Jay Chawla 
# 041816 Bank Module

def bankingProcessing (self, wallet):
    self.wallet = wallet
        
        print("Welcome to the Bank! (use 'WITHDRAW' or 'DEPOSIT')")
        
        
        stillBanking = true
        
        stored = 0
        
        while stillBanking = true:
            
            choice == input('Please select transaction:')
                
                if choice[0] = 'W':
                    wsum = input'(Select the amount you wish to WITHDRAW:)'
                        
                        if wsum <= stored:
                            stored == (stored - wsum)
                                self.wallet == (self.wallet + wsum)
                                
                                print('You have withdrawn %i money. Your current holdings - Wallet: %i - Bank: %i') % (wsum, wallet, stored)
                                cont = input('Would you like to continue? Y/N')
                                if cont = 'Y':
                                
                                elif cont = 'N':
                                    stillBanking == False
                                        break
                    
                        else:
                            print:('You do not have enough funds for this transaction.')
    
            elif choice[0] = 'D':
                dsum = input'(Select the amount you wish to DEPOSIT:)'
                    
                    if dsum <= wallet:
                        stored == (stored + dsum)
                            self.wallet == (self.wallet - dsum)
                                
                                print('You have deposited %i money. Your current holdings - Wallet: %i - Bank: %i') % (dsum, wallet, stored)
                                cont = input('Would you like to continue? Y/N')
                                if cont = 'Y':
                                
                                elif cont = 'N':
                                    stillBanking == False
                                        break
                        
                        else:
                            print:('You do not have enough funds for this transaction.')
            
            
            else:
                print('I am sorry, your transaction could not be processed at this time. Please try again.')
