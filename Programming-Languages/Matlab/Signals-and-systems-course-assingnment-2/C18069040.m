%first part
%read the audio

[tel, fs] = audioread("tel.wav");
figure(1)
tiledlayout(5,2)
nexttile
stem(tel)
title('Normal Sound with Stem')

nexttile
plot(tel)
title('Normal Sound with Plot')

% by plotting the tel, I can find the beginning and the end of the each
% seven number sound
first = tel(1:817);
second = tel(1186:2031);
third = tel(2362:3231);
fourth = tel(4371:5213);
fifth = tel(5587:6413);
sixth = tel(6785:7620);
seventh = tel(7988:8814);

L1 = length(first);
L2 = length(second);
L3 = length(third);
L4 = length(fourth);
L5 = length(fifth);
L6 = length(sixth);
L7 = length(seventh);

sound_values = {first, second, third, fourth, fifth, sixth, seventh};
sound_lengths = {L1, L2, L3, L4, L5, L6, L7};
%       1209   1336    1477
%697    1       2       3
%770    4       5       6
%852    7       8       9
%941    *       0       #
sound_equivalents = ["8", "6", "7", "5", "3", "0", "9"];

for i = 1:length(sound_lengths)
    nexttile
    Y = fft(sound_values{i});
    L = sound_lengths{i};
    P2 = abs(Y/L);
    P1 = P2(1:L/2+1);
    P1(2:end-1) = 2*P1(2:end-1);
    f = fs*(0:(L/2))/L
    plot(f, P1)
    title(sprintf('%d. Sound, Value: %c', i, sound_equivalents(i)))
end


%%%second part%%%
%read my audio

[my_tel, my_fs] = audioread("my_audio.wav")

figure(2)
tiledlayout(7, 2)
nexttile
stem(my_tel)
title('Normal My Sound with Stem')

nexttile
plot(my_tel)
title('Normal My Sound with Plot')

% by plotting the tel, I can find the beginning and the end of the each
% seven number sound
my_first = my_tel(37065:63402);
my_second = my_tel(74100:95674);
my_third = my_tel(109230:129730);
my_fourth = my_tel(144150:163965);
my_fifth = my_tel(181485:198555);
my_sixth = my_tel(220427:242043);
my_seventh = my_tel(257899:275716);
my_eight = my_tel(295309:325286);
my_ninth = my_tel(333957:364662);
my_tenth = my_tel(378459:396713);
my_eleventh = my_tel(414008:437829);

L1 = length(my_first);
L2 = length(my_second);
L3 = length(my_third);
L4 = length(my_fourth);
L5 = length(my_fifth);
L6 = length(my_sixth);
L7 = length(my_seventh);
L8 = length(my_eight);
L9 = length(my_ninth);
L10 = length(my_tenth);
L11 = length(my_eleventh);


my_sound_values = {my_first, my_second, my_third, my_fourth, my_fifth, my_sixth, my_seventh, my_eight, my_ninth, my_tenth, my_eleventh};
my_sound_lengths = {L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11};
%       1209   1336    1477
%697    1       2       3
%770    4       5       6
%852    7       8       9
%941    *       0       #
my_sound_equivalents = ["1", "5", "9", "6", "3", "8", "7", "5", "4", "2", "8"];

for i = 1:length(my_sound_equivalents)
    nexttile
    Y = fft(my_sound_values{i});
    L = my_sound_lengths{i};
    P2 = abs(Y/L);
    P1 = P2(1:L/2+1);
    P1(2:end-1) = 2*P1(2:end-1);
    f = my_fs*(0:(L/2))/L
    plot(f, P1)
    title(sprintf('%d. Sound, Value: %c', i, my_sound_equivalents(i)))
end