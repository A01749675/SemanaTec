from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
from tabulate import tabulate

class Connection():
    def __init__(self) -> None:
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'
        creds = None
        creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        SAMPLE_SPREADSHEET_ID = '1xBixJvwSrsvAbEHCs1-dxzGaCWdJ-78fyU09CmXpwgQ'
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Forms_Raw!A1:E500").execute()
        values = result.get('values', [])
        self.df = pd.DataFrame(values)
        self.df.to_csv('sample.csv')
        self.db = pd.read_csv("parameters.csv")
        self.columns_names = {}
        self.index = {}
        self.componentes = []
