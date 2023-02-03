import("stdfaust.lib");
freq = hslider("frequency[midi:ctrl 11]",200,50,1000,0.01) : si.smoo;

// Q1
process = os.osc(440);

// Q4, need to uncomment each line to generate each sound.
//process = os.sawtooth(440);
//process = os.triangle(440);
//process = os.ba.pulse(440);
//process = no.noise;
