from lxml import etree

def add_pulsing_effect(svg_file):
    tree = etree.parse(svg_file)
    root = tree.getroot()

    # 为蛇体添加脉动效果
    pulse_effect = etree.Element('animate', 
        attributeName="stroke-width",
        from_="2",
        to="10",
        dur="0.5s",
        repeatCount="indefinite")
    snake_path = root.xpath('//path[@class="snake"]')[0]
    snake_path.append(pulse_effect)
    
    # 保存修改后的 SVG 文件
    tree.write(svg_file)

if __name__ == "__main__":
    import sys
    svg_file = sys.argv[1]
    add_pulsing_effect(svg_file)
