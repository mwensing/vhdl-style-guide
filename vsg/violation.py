

class New():

  def __init__(self, iLine, oTokens, sSolution=None):
      self.iLine = iLine
      self.oTokens = oTokens
      self.sSolution = sSolution

  def get_tokens(self):
      return self.oTokens.get_tokens()

  def get_line_number(self):
      return self.iLine

  def set_tokens(self, lTokens):
      self.oTokens.set_tokens(lTokens)

  def set_solution(self, sSolution):
      self.solution = sSolution

  def get_solution(self):
      return self.sSolution
