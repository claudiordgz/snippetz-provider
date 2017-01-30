from lxml import etree


def main():
    with open('sounds.rss', "rb") as f:
        root = etree.XML(f.read())
        tags = root.xpath('//item/enclosure')
        target = open('music_files.txt', 'w')
        for element in tags:
            target.write('url={url}, length={length} \n'.format(url=element.get('url'), length=element.get('length')))
        target.close()


if __name__ == '__main__':
    main()