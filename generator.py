import svgwrite
import sys


def draw_text(file_name, color_name, color):
    dwg = svgwrite.Drawing('colors/' + file_name + '-text.svg', size=(u'180', u'30'))
    dwg.add(dwg.text(color_name + ':' + color, insert=(10, 20), fill=color))
    dwg.save()


def draw_bg(file_name, color):
    dwg = svgwrite.Drawing('colors/' + file_name + '-bg.svg', size=(u'180', u'60'))
    dwg.add(dwg.rect((0, 0), (180, 60), fill=color))
    dwg.save()


if __name__ == '__main__':
    file_name = sys.argv[1]
    color_name = sys.argv[2]
    color = sys.argv[3]

    draw_text(file_name=file_name, color_name=color_name, color=color)
    draw_bg(file_name=file_name, color=color)

    print('---------------------Markdown---------------------')
    print(color_name + '   '
          ' | '
          '<a><img src="https://phodal.github.io/colors/colors/' + file_name + '-text.svg"/></a>          '
          ' | '
          '<a><img src="https://phodal.github.io/colors/colors/' + file_name + '-bg.svg"/></a>')