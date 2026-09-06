"""Build editable 1080 x 1440 SVGs using only Python's standard library."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent
BG, FG, MUTED, ORANGE, LINE, PANEL = '#131414', '#e8e7e3', '#b6b5af', '#d77600', '#41423e', '#1c1e1d'
SERIF, MONO = 'STIX Two Text', 'JetBrains Mono'

class Slide:
    def __init__(self, n, name, light=False):
        self.n,self.name,self.light=n,name,light
        self.ink='#171918' if light else FG
        self.muted='#575952' if light else MUTED
        self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1440" viewBox="0 0 1080 1440"><title>{escape(name)}</title><desc>Pi Coding Agent tutorial by Julius Darang. Slide {n} of 8. Editable vector artwork.</desc>']
        self.rect(0,0,1080,1440,'#eeeae1' if light else BG,id='background')
        self.text('PI / FIELD NOTES',88,79,23,MONO,ORANGE,id='series-label')
        self.text('JULIUS DARANG',992,79,21,MONO,self.muted,anchor='end')
        self.line(88,117,992,117,'#c8c5bb' if light else LINE)
    def text(self, txt,x,y,size=36,font=SERIF,fill=None,weight=400,anchor='start',id=None):
        attrs=f' id="{id}"' if id else ''
        self.parts.append(f'<text{attrs} x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{fill or self.ink}" text-anchor="{anchor}">{escape(txt)}</text>')
    def lines(self,txt,x,y,size=36,leading=48,**kw):
        for i,t in enumerate(txt.split('\n')): self.text(t,x,y+i*leading,size,**kw)
    def rect(self,x,y,w,h,fill,stroke=None,id=None):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="1.5"' if stroke else '')+(f' id="{id}"' if id else '')+'/>')
    def line(self,x1,y1,x2,y2,color=LINE,width=1.5):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')
    def group(self,name):self.parts.append(f'<g id="{name}">')
    def end(self):self.parts.append('</g>')
    def arrow(self,x1,y1,x2,y2,color=ORANGE):
        self.line(x1,y1,x2,y2,color,2)
        if x1==x2:self.line(x2-7,y2-10,x2,y2,color,2);self.line(x2+7,y2-10,x2,y2,color,2)
        else:self.line(x2-10,y2-7,x2,y2,color,2);self.line(x2-10,y2+7,x2,y2,color,2)
    def title(self,kicker,txt):
        self.text(kicker,88,190,24,MONO,ORANGE)
        self.lines(txt,88,295,90,96,weight=500)
    def terminal(self,y,label,lines,size=29,height=None):
        height=height or 114+len(lines)*46
        self.group(label.lower().replace(' ','-'))
        self.rect(88,y,904,height,PANEL,LINE)
        self.text(label,116,y+40,21,MONO,MUTED)
        self.line(88,y+62,992,y+62)
        for i,line in enumerate(lines):self.text(line,116,y+110+i*46,size,MONO,FG)
        self.end()
    def note(self,number,title,body,y):
        self.group('note-'+number)
        self.text(number,88,y,24,MONO,ORANGE)
        self.text(title,159,y,42,weight=500)
        self.lines(body,159,y+55,34,45,fill=self.muted)
        self.end()
    def cube(self,x,y,k=1,color=FG):
        self.parts.append(f'<g transform="translate({x} {y}) scale({k})" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round">')
        self.parts.append('<path d="M 0 0 L 78 -34 L 154 0 L 76 37 Z" opacity=".55"/><path d="M 0 0 V 112 L 76 151 L 154 112 V 0 M 76 37 V 151" opacity=".9"/>')
        self.end()
    def save(self):
        self.group('footer')
        self.line(88,1321,992,1321,'#c8c5bb' if self.light else LINE)
        self.text('@juliusdarang',88,1375,23,MONO,self.muted)
        self.text(f'{self.n:02} / 08',992,1375,23,MONO,self.muted,anchor='end')
        for i in range(8):self.rect(438+i*26,1361,14,3,ORANGE if i==self.n-1 else ('#c8c5bb' if self.light else LINE))
        self.end();self.parts.append('</svg>')
        (OUT/f'{self.n:02}-{self.name}.svg').write_text('\n'.join(self.parts)+'\n')

s=Slide(1,'meet-pi')
s.text('Meet Pi.',88,316,160,weight=500)
s.lines('Your coding agent.\nYour way of working.',92,397,48,61,fill=MUTED)
s.group('cover-cube-grid')
for row in range(3):
    for col in range(3):s.cube(234+col*208,600+row*174,1.15,ORANGE if (row,col)==(1,1) else FG)
s.end()
s.text('A PRACTICAL STARTER GUIDE',88,1190,24,MONO,ORANGE)
s.text('From first prompt to a change you can verify.',88,1246,37)
s.save()

s=Slide(2,'small-core')
s.title('THE IDEA','A small core.\nRoom to make it yours.')
s.lines('Pi connects a model to your project\nthrough a few visible tools.',88,487,39,52,fill=MUTED)
s.group('tool-grid')
for x,y,name,verb,detail in [(88,641,'read','Inspect','Files and images'),(554,641,'write','Create','New or replacement files'),(88,854,'edit','Patch','Focused file changes'),(554,854,'bash','Run','Commands and checks')]:
    s.rect(x,y,438,185,PANEL)
    s.line(x,y,x,y+185,ORANGE,3)
    s.text(name,x+28,y+49,30,MONO,ORANGE)
    s.text(verb,x+28,y+105,47)
    s.text(detail,x+28,y+151,29,fill=MUTED)
s.end()
s.text('You define the goal. Pi works through the tools.',88,1140,35)
s.text('Skills and extensions let you shape the workflow.',88,1192,35,fill=MUTED)
s.save()

s=Slide(3,'get-running')
s.title('01 / SET UP','Start in\nyour project.')
s.text('Have Node.js, npm, and a model provider ready.',88,471,35,fill=MUTED)
s.terminal(527,'SHELL', ['npm install -g --ignore-scripts \\', '  @earendil-works/pi-coding-agent','','cd /path/to/your/project','pi'],29,342)
s.terminal(907,'INSIDE PI',['/login','/model'],33,196)
s.lines('Sign in to a provider, then choose a model.\nThe directory you launch from is your workspace.',88,1171,35,48,fill=MUTED)
s.save()

s=Slide(4,'inspect-first')
s.title('02 / FIRST PROMPT','Let it look\nbefore it edits.')
s.text('Begin with a request you can check.',88,478,39,fill=MUTED)
s.group('inspection-prompt');s.line(88,551,88,820,ORANGE,4)
s.text('TRY THIS PROMPT',120,587,23,MONO,ORANGE)
s.lines('Summarize this repository.\nFind the entry points and tests.\nTell me how to run the checks.\nDo not edit anything yet.',120,662,42,57)
s.end()
s.note('A','Read the answer.','Does it name real files and commands?',950)
s.note('B','Check the evidence.','Open the files. Read the tool output.',1120)
s.save()

s=Slide(5,'bound-the-task')
s.title('03 / MAKE A CHANGE','One task.\nA clear finish line.')
s.text('Give Pi a result and the rules for getting there.',88,478,36,fill=MUTED)
s.group('bounded-task-example')
s.rect(88,551,904,508,PANEL,LINE)
s.text('EXAMPLE / CSV IMPORTER',120,600,23,MONO,ORANGE)
s.text('Add validation for invalid CSV rows.',120,675,43)
s.line(120,709,960,709)
for y,label,copy in [(769,'KEEP','Preserve the public API.'),(846,'AVOID','No new runtime dependency.'),(923,'PROVE','Run the existing importer tests.')]:
    s.text(label,120,y,23,MONO,ORANGE);s.text(copy,268,y,36)
s.text('First explain the plan. Then make the change.',120,1015,33,fill=MUTED)
s.end()
s.lines('A useful prompt makes success observable.\nName what must change—and what must hold.',88,1161,37,51,fill=MUTED)
s.save()

s=Slide(6,'verify-the-work')
s.title('04 / VERIFY','The diff is\npart of the answer.')
s.text('Read what changed. Run the project’s checks.',88,478,37,fill=MUTED)
s.terminal(540,'SHELL / REVIEW',['git diff','git diff --check'],36,209)
s.note('01','Run the relevant tests.','Use the commands your project actually uses.',857)
s.note('02','Compare with the requirement.','Did the change satisfy the acceptance criteria?',1011)
s.text('Commit only what you understand.',88,1224,45,fill=ORANGE)
s.save()

s=Slide(7,'make-it-yours')
s.title('05 / SHAPE THE WORKFLOW','Stop repeating\nyour project rules.')
s.text('Put durable instructions in AGENTS.md.',88,478,39,fill=MUTED)
s.terminal(545,'AGENTS.md / EXAMPLE',['# Project rules','','- Run npm run check after edits.','- Do not edit generated files.','- Keep the public API stable.'],30,335)
s.terminal(921,'INSIDE PI / RELOAD RULES',['/reload'],35,153)
s.lines('Next: turn a repeated procedure into a skill.\nAdd an extension when you need custom behavior.',88,1162,35,49,fill=MUTED)
s.save()

s=Slide(8,'get-the-guide',True)
s.text('GO FROM STARTER TO WORKFLOW',88,190,23,MONO,ORANGE)
s.lines('Build your own\nPi workflow.',88,299,102,111,weight=500)
s.group('guide-cover')
s.rect(88,492,331,450,'#090b0a')
s.text('PI CODING AGENT',113,533,16,MONO,ORANGE)
s.text('Pi Agent',113,598,49,SERIF,FG,500)
for row in range(2):
    for col in range(2):s.cube(138+col*115,691+row*107,.65,FG)
s.text('JULIUS DARANG',113,912,14,MONO,MUTED)
s.end()
s.text('THE COMPLETE GUIDE',474,540,22,MONO,ORANGE)
s.text('28 lessons.',474,614,58,weight=500)
s.lines('Setup & first tasks\nProject rules & skills\nSessions & automation\nExtensions & the SDK',474,692,34,58)
s.text('A practical PDF by Julius Darang.',88,1003,33,fill=s.muted)
s.line(88,1054,992,1054,'#c8c5bb')
s.text('DM me “PI”',88,1165,100,weight=500)
s.text('for the full guide.',91,1234,48)
s.arrow(893,1193,992,1193,'#171918')
s.save()
print('Built 8 editable SVG slides at 1080 x 1440.')
