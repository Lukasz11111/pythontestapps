import os
import time
class CustomCode:
    def createNewPyFile(self,nameFile, replyCode, howMany, endCode,imports):
        with open(f'{nameFile}.py', 'w') as f:
            code=imports
            print(howMany)
            howMany=int(howMany)
            for x in range(0,howMany):
                code=code+f'''
{replyCode}'''
            code=code+f'''
{endCode}'''
            f.write(code)
    
    def deleteFile(self,nameFile):
        os.remove(f'''{nameFile}.py''')
    
    def main(self, nameFile, replyCode, howMany,endCode, imports,useTry):
        self.createNewPyFile(nameFile, replyCode, howMany,endCode,imports)
        self.start( nameFile,useTry)
        # self.deleteFile(nameFile)
        print('done')


    def start(self,nameFile, useTry):
        import sys
        sys.path.append(".")
        {
        '0': self.tryNotDoOrDoNot(nameFile),
        '1': self.useTry(nameFile)
        }[useTry]
            
    def useTry(self, nameFile):
        try:
            __import__(nameFile)
        except:
            pass
    
    def tryNotDoOrDoNot(self,nameFile):
        __import__(nameFile)
        
    def codeGenDef(self, defCount, codeInDef):
        for a in range(0,defCount):
            if a>0:
                code=code+f'''
def a{a}():
    {codeInDef}
    a{a-1}()'''
            else:
                code=f'''
def a{a}():
    {codeInDef}
    print("aaa")'''
        code=code+f'''
a{a}()
'''
        return code



