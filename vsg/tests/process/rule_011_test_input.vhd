
architecture RTL of FIFO is

begin

  process is
  begin
  end process;

  process
  begin
  end process;

  -- Violations below
  process is begin
  end process;
  a <= b;

  process begin
  end process;
  b <= z;

end architecture RTL;
