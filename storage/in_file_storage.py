class InFileStorage:
    def __init__(self, filename):
        self.filename = filename

    def save(self, guid, url, value):
        with open(self.filename, 'a') as f:
            f.write(f'{guid} {url} {value}\n')

    def get(self, guid):
        with open(self.filename) as f:
            for line in f.readlines():
                g, u, v = line.strip().split(' ')
                if g == guid:
                    return v
