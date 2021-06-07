from collections import defaultdict
import re
import gzip

class BedFinder(object):
    '''
        For a given BED file, read into memory and search on location.
    '''

    _reg_split = re.compile(r'''[:-]''')
    _window = 100000

    def __init__(self, bed):
        '''
            Opens given bed file, reads into memory and sorts by
            coordinate for efficient retrieval by coordinate.
        '''
        self.regions = defaultdict(dict)
        if bed.endswith((".gz", ".bgz")):
            bfile = gzip.open(bed, errors='replace', mode='rt')
        else:
            bfile = open (bed, 'rt')
        for line in bfile:
            if line[0] == '#': continue
            s = line.rstrip().split("\t")
            if len(s) < 3:
                raise BedFormatError("Not enough fields in BED line: " + line)
            try:
                s[1] = int(s[1])
                s[2] = int(s[2])
            except ValueError:
                raise BedFormatError("Columns 2 and 3 must be integers (for " +
                                     "line: "+ line + ")")
            r_start = int(s[1]/self._window) * self._window
            r_end = int(s[2]/self._window) * self._window
            for i in range(r_start, r_end + self._window, self._window):
                if i not in self.regions[s[0]]:
                    self.regions[s[0]][i] = list()
                self.regions[s[0]][i].append(s)
        bfile.close()
        for c in self.regions:
            for i in self.regions[c]:
                self.regions[c][i].sort(key=lambda x: (x[1], x[2]))

    def fetch_region(self, region):
        ''' Fetch lines overlapping given region (in format chr1:1-2000) '''
        c, s, e = self._reg_split.split(region)
        return self.fetch(c, s, e)

    def fetch(self, chrom, start, end):
        '''
            Fetch lines overlapping given chromosome, start and end
            coordinates.
        '''
        if chrom not in self.regions:
            return []
        start = int(start)
        end = int(end)
        idx_start = int(start/self._window) * self._window
        idx_end = int(end/self._window) * self._window
        candidates = []
        hits = []
        if idx_start in self.regions[chrom]:
            candidates.extend(self.regions[chrom][idx_start])
        if idx_end != idx_start and idx_end in self.regions[chrom]:
            candidates.extend(self.regions[chrom][idx_end])
        for reg in candidates:
            if start <= reg[2] and end > reg[1]:
                hits.append(reg)
            elif end <= reg[1]:
                break
        return hits


class BedFormatError(Exception):
    pass
