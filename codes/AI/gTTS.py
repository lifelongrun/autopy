from gtts import gTTS

text = ("""

Listen to part of a lecture in an environmental engineering class.

At the end of yesterday's class, we were discussing landfills and the hundreds and millions of tons of everyday garbage which are deposited into them each year in the United States.

It's a growing problem.

Quite simply, we're running out of space to put our garbage.

And this is especially true for solid organic waste.

Food scraps from home or food processing plants.

Waste from farms.

That sort of thing.

Did you know that two-thirds of the waste sitting in our landfills is organic material?

We have government recycling programs for materials like plastic, glass, and metal.

Yet widespread solutions for organic waste materials haven't really been addressed in the United States.

I think this is just asking for trouble in the future.

So today, I want to talk about a technology that offers a potential solution to the problem.

Anaerobic Phased Solids Digestion, or APS digestion.

First of all, what does anaerobic mean?

Anyone?

Without oxygen?

Correct.

APS digestion uses anaerobic bacteria, ones that thrive in the absence of oxygen, to consume, to break down organic material.

Excuse me, professor.

Those anaerobic bacteria you're talking about, well, aren't anaerobic bacteria also used in wastewater treatment plants?

Yes, in fact they are.

Would you like to explain this to the class?

Sure.

So, when wastewater is treated, one of the byproducts is a thick liquid called sludge, and aren't anaerobic bacteria used to break down the sludge?

That's right.

Anaerobic bacteria have been used in wastewater treatment for decades.

So how is this technology different?

Good question.

The anaerobic digestion systems used in wastewater plants are designed to treat sludge, not solids.

Now, in the past, researchers have attempted to treat solid organic waste with that same equipment.

But there was always a problem.

In order to process the solid waste, the kind we find in landfills, you had to pre-treat the solids to turn them into sludge.

First, by breaking the material apart mechanically into small particles, and then adding a lot of water, until you got a kind of thick, soupy mix that the equipment could handle.

But that extra step took time and required a lot of energy.

That sounds like it would cost a lot.

That's right.

But APS digestion is designed specifically to handle solid waste.

So it's much more cost effective.

The new technology processes organic waste in two phases.

Remember, APS stands for anaerobic phased solid digestion.

First, the waste material is loaded into a large, closed container, along with different types of anaerobic bacteria.

The bacteria break the solids down into acids and hydrogen gas.

The hydrogen is extracted, and the remaining acids are transferred into a different container for the second phase of the process.

There, another type of bacteria converts the acids into methane gas.

Aren't hydrogen and methane gas bad for the environment, though?

The answer in this case is no, because they don't escape into the atmosphere.

The gases are captured and can be burned to produce electricity, which saves a lot of money, and ultimately decreases our need for fuels like petroleum and coal, which are not only expensive but are also polluting.

So organic waste from landfills could be processed this way?

It's certainly one possibility.

And APS digestion systems are very versatile.

They can be installed just about anywhere.

See, anaerobic digestion systems used at wastewater treatment plants are huge tanks that hold thousands of gallons of wastewater.

But the APS containers are small enough to be set up on-site, where the waste is generated, like at food processing plants or on farms.

So garbage doesn't have to be transported long distances.

As a matter of fact, a couple of universities successfully set up demonstration projects.

They collected food scraps from dining halls and local restaurants and processed them in APS facilities.

Not only did the university save money, we're also learning even more about the APS process.

What's the next step forward?

Well, APS digestion uses several different types of anaerobic bacteria, right?

So what are the most efficient bacteria in the process?

If researchers can figure that out, the highest performing bacteria mix for a system could be determined.

Ultimately, the goal would be to grow enough of these particular bacteria to support large-scale commercial APS systems.

我的笔记
""")
tts = gTTS(text, lang='en')
tts.save("output-TPO-34-C2.mp3")
