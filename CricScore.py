from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk
from bs4 import BeautifulSoup
import requests
import re


class CricScore :
    
    def __init__(self,rootWindow):
        self.rootWindow = rootWindow
        self.rootWindow.title("LIVE CRICKET SCORE")
        self.rootWindow.geometry('800x500')
        self.bg = ImageTk.PhotoImage(file="cric_msd1.jpg")
        bg = Label(self.rootWindow, image=self.bg).place(x=0, y=0)

        self.label = Label(self.rootWindow, text='Live Matches', font=("times new roman", 60), compound='center').pack(padx=100, pady=50)
        

        self.var = StringVar()
        self.matches = self.match_details()
        self.data = [i for i in self.matches.keys()]
        self.cb = Combobox(self.rootWindow, values = self.data, width = 50)
        self.cb.place(x=250, y=200)

        self.b1 = Button(self.rootWindow, text="Check Score", font=("times new roman", 15), command = self.show_match_details).place(x=50, y=380)

    def select(self):
        return self.cb.get()

    # scrapping the data from cricbuzz.com
    def scrap(self):
        URL = "https://www.cricbuzz.com/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="match_menu_container")
        scrap_results = results.find_all("li", class_="cb-match-card")
        return scrap_results

    # Load the cricket match details
    def match_details(self):
        details = self.scrap()
        live_match = {}
        for detail in details:
            live_team_details = {}
            summary = self.match_summary(detail)
            if summary is not None:
                match_header = self.match_header(detail).text
                teams = self.teams_name(detail)
                score_card = self.team_score(detail)
                live_team_details['summary'] = summary.text
                live_team_details['match_header'] = match_header
                live_team_details['score_card'] = score_card[0] + " :: " + score_card[1]
                live_match[teams[0] + " vs " + teams[1]] = live_team_details
        
        return live_match

    def match_summary(self, detail):
        return detail.find("div",class_="cb-mtch-crd-state")

    def match_header(self, detail):
        return detail.find("div", class_="cb-mtch-crd-hdr")

    
    def team_score(self, detail):
        t = []
        team1_details = detail.find("div", class_="cb-hmscg-bat-txt").text
        team2_details = detail.find("div", class_="cb-hmscg-bwl-txt").text
        t.append(team1_details)
        t.append(team2_details)
        return t

    def teams_name(self,detail):
        t=[]
        team1_details = detail.find("div", class_="cb-hmscg-bat-txt").text
        team1_index = re.search(r"\d", team1_details).start() if re.search(r"\d", team1_details) else len(team1_details)
        
        team2_details = detail.find("div", class_="cb-hmscg-bwl-txt").text
        team2_index = re.search(r"\d", team2_details).start() if re.search(r"\d", team2_details) else len(team2_details)
        
        t.append(team1_details[:team1_index])
        t.append(team2_details[:team2_index])
        return t

     # Present details in  gui
    def show_match_details(self):

        # Building match details frame
        self.frame1 = Frame(self.rootWindow, bg="#ADD8E6")
        self.frame1.place(x=180, y=280, width=600, height=200)

        # Fetching details of match
        x = self.matches[self.select()]

        
        # Displaying team names
        Label(self.frame1, text=self.select() + " - " + x['match_header'], font=("times new roman", 15, "bold"), bg="#ADD8E6", fg="red",
                      bd=0).place(x=10, y=15)

       
        # Dispalying details of the match
        Label(self.frame1, text="Score Details : ", font=("times new roman", 10, "bold"), bg="#ADD8E6", fg="black",
              bd=0).place(x=10, y=40)
        Label(self.frame1, text=x['score_card'], font=("times new roman", 10, "bold"), bg="#ADD8E6", fg="black",
              bd=0).place(x=20, y=60)
        
        Label(self.frame1, text="Summary : ", font=("times new roman", 10, "bold"), bg="#ADD8E6", fg="black",
              bd=0).place(x=10, y=100)
        Label(self.frame1, text=x['summary'], font=("times new roman", 10, "bold"), bg="#ADD8E6", fg="black",
              bd=0).place(x=20, y=120)
#main function 
def main():
    #GUI start
    rootWindow = Tk()
    
    #fetching data
    obj = CricScore(rootWindow)
    
    #keeps window on 
    rootWindow.mainloop()
    
if __name__ == '__main__':
    main()
    
    