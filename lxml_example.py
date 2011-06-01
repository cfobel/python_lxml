from lxml.builder import E
from lxml import etree

if __name__ == '__main__':
    test = (E.root(
                E.configuration(
                        E.param("ITEM1: p1"),
                        E.param("ITEM1: p2"),
                        E.param("ITEM1: p3"),
                    name='Config 1'), 
                E.configuration(
                        E.param("ITEM2: p1"),
                        E.param("ITEM2: p2"),
                        E.param("ITEM2: p3"),
                        E.param("ITEM2: p4"),
                    name='Config 2'),
            ))
    data = etree.tostring(test, pretty_print=True, xml_declaration=True)

    print data

    root = etree.XML(data)

    configs = root.xpath('//configuration')

    for c in configs:
        params = c.xpath('param')
        print '%s attrs=%s' % (c.tag, c.attrib)
        for p in params:
            print '  %s' % p.text
