
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;



entity ctfdecoder is
    Port ( Q : in  STD_LOGIC_VECTOR (6 downto 0);
           two : out  STD_LOGIC;
           three : out  STD_LOGIC;
           four : out  STD_LOGIC;
           five : out  STD_LOGIC;
           seven : out  STD_LOGIC;
           underscore : out  STD_LOGIC;
           c : out  STD_LOGIC;
           d : out  STD_LOGIC;
           h : out  STD_LOGIC;
           k : out  STD_LOGIC;
           u : out  STD_LOGIC;
           w : out  STD_LOGIC);
end ctfdecoder;

architecture Dataflow of ctfdecoder is

begin
two <= ((not Q(6)) and Q(5) and Q(4) and (not Q(3)) and (not Q(2)) and Q(1) and (not Q(0)));
three <= ((not Q(6)) and Q(5) and Q(4) and (not Q(3)) and (not Q(2)) and Q(1) and Q(0));
four <= ((not Q(6)) and Q(5) and Q(4) and (not Q(3)) and Q(2) and (not Q(1)) and (not Q(0)));
five <= ((not Q(6)) and Q(5) and Q(4) and (not Q(3)) and Q(2) and (not Q(1)) and Q(0));
seven <= ((not Q(6)) and Q(5) and Q(4) and (not Q(3)) and Q(2) and Q(1) and Q(0));
underscore <= (Q(6) and (not Q(5)) and Q(4) and Q(3) and Q(2) and Q(1) and Q(0));
c <= (Q(6) and Q(5) and (not Q(4)) and (not Q(3)) and (not Q(2)) and Q(1) and Q(0));
d <= (Q(6) and Q(5) and (not Q(4)) and (not Q(3)) and Q(2) and (not Q(1)) and (not Q(0)));
h <= (Q(6) and Q(5) and (not Q(4)) and Q(3) and (not Q(2)) and (not Q(1)) and (not Q(0)));
k <= (Q(6) and Q(5) and (not Q(4)) and Q(3) and (not Q(2)) and Q(1) and Q(0));
u <= (Q(6) and Q(5) and Q(4) and (not Q(3)) and Q(2) and (not Q(1)) and Q(0));
w <= (Q(6) and Q(5) and Q(4) and (not Q(3)) and Q(2) and Q(1) and Q(0));

end Dataflow;

