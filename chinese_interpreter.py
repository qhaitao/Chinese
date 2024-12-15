import svgwrite
from svgwrite import cm, mm
import random
import textwrap

class ChineseInterpreter:
    def __init__(self):
        self.width = 400
        self.height = 600
        self.margin = 20
        self.background_colors = ['#F4F1DE', '#E07A5F', '#3D405B', '#81B29A']

    def create_svg_card(self, word, interpretation):
        dwg = svgwrite.Drawing(f'{word}_card.svg', size=(f'{self.width}px', f'{self.height}px'))
        
        # Background
        dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill=self.background_colors[0]))
        
        # Title
        dwg.add(dwg.text('汉语新解', insert=(self.width/2, 50), 
                        font_family="KingHwa_OldSong", font_size=32, 
                        text_anchor="middle", fill='#3D405B'))
        
        # Word
        dwg.add(dwg.text(word, insert=(self.width/2, 120),
                        font_family="KingHwa_OldSong", font_size=48,
                        text_anchor="middle", fill='#E07A5F'))
        
        # Divider
        dwg.add(dwg.line(start=(self.margin, 150), end=(self.width-self.margin, 150),
                        stroke='#3D405B', stroke_width=1))
        
        # Interpretation
        y_pos = 200
        wrapped_text = textwrap.wrap(interpretation, width=20)
        for line in wrapped_text:
            dwg.add(dwg.text(line, insert=(self.width/2, y_pos),
                            font_family="KingHwa_OldSong", font_size=20,
                            text_anchor="middle", fill='#3D405B'))
            y_pos += 30
        
        # Decorative elements
        self._add_geometric_patterns(dwg)
        
        return dwg

    def _add_geometric_patterns(self, dwg):
        # Add some minimal geometric decorations
        patterns = dwg.defs.add(dwg.g(id='patterns'))
        for i in range(3):
            x = random.randint(self.margin, self.width-self.margin)
            y = random.randint(400, self.height-self.margin)
            size = random.randint(10, 30)
            dwg.add(dwg.rect(insert=(x, y), size=(size, size),
                            fill='none', stroke='#81B29A', stroke_width=1,
                            transform=f'rotate({random.randint(0, 45)}, {x}, {y})'))

def generate_card(word):
    interpreter = ChineseInterpreter()
    
    # 讽刺性的解释
    if word == "房子":
        interpretation = """
        一个四方的梦，
        装满三十年的未来。
        人们把它叫做避风港，
        却在按揭里逆风航行。
        这是最沉重的羽毛。
        """
    elif word == "财富":
        interpretation = """
        这个词总让人想起数字，
        却忘了数字本是人造的幻象。
        把快乐装进银行，
        却在提款机前痛哭。
        多么现代的魔法啊。
        """
    elif word == "牛羊":
        interpretation = """
        从前牛羊是财富的象征，
        如今却成了形容温顺的代名词。
        赞美你像牛羊一样驯服，
        其实是在夸你不会思考。
        多么甜蜜的陷阱啊。
        """
    else:
        interpretation = """
        现代社会的隐喻符号。
        表面是褒义的生产力象征，
        实则暗指被压榨的劳动者。
        这对字眼儿把人说成了牲口，
        还美其名曰：吃苦耐劳。
        """
    
    dwg = interpreter.create_svg_card(word, interpretation.strip())
    dwg.save()
    return f'{word}_card.svg'

if __name__ == "__main__":
    generate_card("房子")
