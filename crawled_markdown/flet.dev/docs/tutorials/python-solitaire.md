[Skip to main content](https://flet.dev/docs/tutorials/python-solitaire/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/tutorials/python-solitaire/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/tutorials/python-solitaire/)
  * [Tutorials](https://flet.dev/docs/tutorials)
    * [To-Do app](https://flet.dev/docs/tutorials/python-todo)
    * [Calculator app](https://flet.dev/docs/tutorials/python-calculator)
    * [Trello clone](https://flet.dev/docs/tutorials/trello-clone)
    * [Solitaire game](https://flet.dev/docs/tutorials/python-solitaire)
    * [Chat app](https://flet.dev/docs/tutorials/python-chat)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * Solitaire game


On this page
# Creating Solitaire game with Python and Flet - Part 1
In this tutorial we will show you step-by-step creation of a famous Klondike solitaire game in Python with Flet. For an inspiration, we looked at this online game: <https://www.solitr.com/>
This tutorial is aimed at beginner/intermediate level Python developers who have basic knowledge of Python and object oriented programming.
Here you can see the final result that you are going to achieve with Flet and this tutorial: <https://gallery.flet.dev/solitaire/>
![](https://flet.dev/img/docs/solitaire-tutorial/part1_final.gif)
We have broken down the game implementation into the following steps:
  * [Getting started with Flet](https://flet.dev/docs/tutorials/python-solitaire/#getting-started-with-flet)
  * [Proof of concept app for draggable cards](https://flet.dev/docs/tutorials/python-solitaire/#proof-of-concept-app-for-draggable-cards)
  * [Fanned card piles](https://flet.dev/docs/tutorials/python-solitaire/#fanned-card-piles)
  * [Solitaire setup](https://flet.dev/docs/tutorials/python-solitaire/#solitaire-setup)
  * [Solitaire rules](https://flet.dev/docs/tutorials/python-solitaire/#solitaire-rules)
  * [Winning the game](https://flet.dev/docs/tutorials/python-solitaire/#winning-the-game)
  * [Deploying the app](https://flet.dev/docs/tutorials/python-solitaire/#deploying-the-app)


In the Part 2 (will be covered in the next tutorial) we'll be adding Appbar with options to start new game, view game rules and change game settings.
## Getting started with Flet[​](https://flet.dev/docs/tutorials/python-solitaire/#getting-started-with-flet "Direct link to Getting started with Flet")
To create a multi-platform app in Python with Flet, you don't need to know HTML, CSS or JavaScript, but you do need a basic knowledge of Python and object-oriented programming.
Before you can create your first Flet app, you need to [setup your development environment](https://flet.dev/docs/getting-started/), which requires Python 3.9 or above and `flet` package.
Once you have Flet installed, let's [create](https://flet.dev/docs/getting-started/create-flet-app) a simple hello-world app.
Create `hello.py` with the following contents:
```
import flet as ftdefmain(page: ft.Page):  page.add(ft.Text(value="Hello, world!"))ft.app(main)
```

Run this app and you will see a new window with a greeting:
![](https://flet.dev/img/docs/tutorial/todo-app-hello-world.png)
## Proof of concept app for draggable cards[​](https://flet.dev/docs/tutorials/python-solitaire/#proof-of-concept-app-for-draggable-cards "Direct link to Proof of concept app for draggable cards")
For the proof of concept, we will only be using three types of controls:
  * [Stack](https://flet.dev/docs/controls/stack) - will be used as a parent control for absolute positioning of slots and cards
  * [GestureDetector](https://flet.dev/docs/controls/gesturedetector) - the card that will be moved within the Stack
  * [Container](https://flet.dev/docs/controls/container) - the slot where the card will be dropped. Also will be used as `content` for the GestureDetector.


We have broken down the proof of concept app into four easy steps, so that after each step you have a complete short program to run and test.
### Step 1: Drag the card around[​](https://flet.dev/docs/tutorials/python-solitaire/#step-1-drag-the-card-around "Direct link to Step 1: Drag the card around")
In this step we will create a `Stack` (Solitaire game field) and a `GestureDetector` (Solitaire card). The card will then be added to the list of the Stack `controls`. `Top` and `left` properties of the GestureDetector are used for absolute positioning of the card in the Stack.
```
import flet as ftdefmain(page: ft.Page):  card = ft.GestureDetector(    left=0,    top=0,    content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),)  page.add(ft.Stack(controls=[card], width=1000, height=500))ft.app(main)
```

Run the app to see the the card added to the stack:
![](https://flet.dev/img/docs/solitaire-tutorial/drag_and_drop1.png)
To be able to move the card, we'll create a `drag` method that will be called in `on_pan_update` event of GestureDetector which happens every `drag_interval` while the user drags the card with their mouse.
To show the card's movement, we’ll be updating the card’s `top` and `left` properties in the `drag` method each time the `on_pan_update` event happens.
Below is the simplest code for dragging GestureDetector in Stack:
```
import flet as ft# Use of GestureDetector for with on_pan_update event for dragging card# Absolute positioning of controls within stackdefmain(page: ft.Page):defdrag(e: ft.DragUpdateEvent):    e.control.top =max(0, e.control.top + e.delta_y)    e.control.left =max(0, e.control.left + e.delta_x)    e.control.update()  card = ft.GestureDetector(    mouse_cursor=ft.MouseCursor.MOVE,    drag_interval=5,    on_pan_update=drag,    left=0,    top=0,    content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),)  page.add(ft.Stack(controls=[card], width=1000, height=500))ft.app(main)
```

Now you can see the card moving:
![](https://flet.dev/img/docs/solitaire-tutorial/drag_and_drop2.gif)
note
After any properties of a control are updated, an `update()` method of the control (or its parent control) should be called for the update to take effect.
### Step 2: Drop the card in the slot or bounce it back[​](https://flet.dev/docs/tutorials/python-solitaire/#step-2-drop-the-card-in-the-slot-or-bounce-it-back "Direct link to Step 2: Drop the card in the slot or bounce it back")
The goal of this step is to be able to drop a card into a slot if it is close enough and bounce it back if it’s not.
![](https://flet.dev/img/docs/solitaire-tutorial/drag_and_drop3.gif)
Let’s create a `Container` control that will represent a slot to which we’ll be dropping the card:
```
slot = ft.Container(  width=70, height=100, left=200, top=0, border=ft.border.all(1))page.add(ft.Stack(controls =[slot, card], width=1000, height=500))
```

`on_pan_end` event of the card is called when the card is dropped:
```
card = ft.GestureDetector(  mouse_cursor=ft.MouseCursor.MOVE,  drag_interval=5,  on_pan_update=drag,  on_pan_end=drop,  left=0,  top=0,  content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),)
```

On this event, we’ll call `drop` method to check if the card is close enough to the slot (let’s say it’s closer than 20px to the slot), and `place` it there:
```
defdrop(e: ft.DragEndEvent):if(abs(e.control.top - slot.top)<20andabs(e.control.left - slot.left)<20):    place(e.control, slot)  e.control.update()defplace(card, slot):"""place card to the slot"""  card.top = slot.top  card.left = slot.left  page.update()
```

Now, if the card is not close enough, we need to bounce it back to its original position. Unfortunately, we don’t know the original position coordinates, since the card’s `top` and `left` properties were changed on `on_pan_update` event.
To solve this problem, let’s create a `Solitaire` class object to keep track of the original position of the card when `on_pan_start` event of the card is called:
```
classSolitaire:def__init__(self):    self.start_top =0    self.start_left =0solitaire = Solitaire()defstart_drag(e: ft.DragStartEvent):  solitaire.start_top = e.control.top  solitaire.start_left = e.control.left  e.control.update()
```

Now let’s update `on_pan_end` event with the option to bounce card back:
```
defbounce_back(game, card):"""return card to its original position"""  card.top = game.start_top  card.left = game.start_left  page.update()defdrop(e: ft.DragEndEvent):if(abs(e.control.top - slot.top)<20andabs(e.control.left - slot.left)<20):    place(e.control, slot)else:    bounce_back(solitaire, e.control)  e.control.update()
```

The full code for this step can be found [here](https://github.com/flet-dev/examples/blob/main/python/tutorials/solitaire/solitaire-drag-and-drop/step2.py).
### Step 3: Adding a second card[​](https://flet.dev/docs/tutorials/python-solitaire/#step-3-adding-a-second-card "Direct link to Step 3: Adding a second card")
Eventually, we’ll need 52 cards to play the game. For our proof of concept, let’s add a second card:
```
  card2 = ft.GestureDetector(    mouse_cursor=ft.MouseCursor.MOVE,    drag_interval=5,    on_pan_start=start_drag,    on_pan_update=drag,    on_pan_end=drop,    left=100,    top=0,    content=ft.Container(bgcolor=ft.Colors.YELLOW, width=70, height=100),)  controls =[slot, card1, card2]  page.add(ft.Stack(controls=controls, width=1000, height=500))
```

Now, if you run the app with the two cards, you will notice that when you move the cards around, the yellow card (card2) is moving as expected but the green the card (card1) is moving under the yellow card.
![](https://flet.dev/img/docs/solitaire-tutorial/drag_and_drop4.gif)
It happens because card2 is added to the list of stack `controls` after card1. To fix this problem, we need to move the draggable card to the top of the list of controls on `on_pan_start` event:
```
defmove_on_top(card, controls):"""Moves draggable card to the top of the stack"""  controls.remove(card)  controls.append(card)  page.update()defstart_drag(e: ft.DragStartEvent):  move_on_top(e.control, controls)  solitaire.start_top = e.control.top  solitaire.start_left = e.control.left
```

Now the two cards can be dragged without issues:
![](https://flet.dev/img/docs/solitaire-tutorial/drag_and_drop5.gif)
The full code for this step can be found [here](https://github.com/flet-dev/examples/blob/main/python/tutorials/solitaire/solitaire-drag-and-drop/step3.py).
### Step 4: Adding more slots[​](https://flet.dev/docs/tutorials/python-solitaire/#step-4-adding-more-slots "Direct link to Step 4: Adding more slots")
As a final step for the proof of concept app, let’s create two more slots:
```
slot0 = ft.Container(  width=70, height=100, left=0, top=0, border=ft.border.all(1))slot1 = ft.Container(  width=70, height=100, left=200, top=0, border=ft.border.all(1))slot2 = ft.Container(  width=70, height=100, left=300, top=0, border=ft.border.all(1))slots =[slot0, slot1, slot2]
```

When creating new cards, we’ll will not specify their `top` and `left` position now, but instead, will place them to the `slot0`:
```
# deal cardsplace(card1, slot0)place(card2, slot0)
```

`on_pan_end` event, where we check if a card is close to a slot, we will now go through the list of slots to find where the card should be dropped:
```
defdrop(e: ft.DragEndEvent):for slot in slots:if(abs(e.control.top - slot.top)<20andabs(e.control.left - slot.left)<20):      place(e.control, slot)      e.control.update()return  bounce_back(solitaire, e.control)  e.control.update()
```

As a result, the two cards can be dragged between the three slots:
![](https://flet.dev/img/docs/solitaire-tutorial/drag_and_drop6.gif)
The full code for this step can be found [here](https://github.com/flet-dev/examples/blob/main/python/tutorials/solitaire/solitaire-drag-and-drop/step4.py).
Congratulations on completing the proof of concept app for the Solitaire game! Now you can work with `GestureDetector` to move cards inside `Stack` and place them to certain `Containers`, which is a great part of the game to begin with.
## Fanned card piles[​](https://flet.dev/docs/tutorials/python-solitaire/#fanned-card-piles "Direct link to Fanned card piles")
In the proof of concept app you have accomplished the task of dropping a card into a slot in proximity or bounce it back. If there is already a card in that slot, the new card is placed on top of it, covering it completely.
In the actual Solitaire game, if there is already a card in a _tableau_ slot, you want to place the draggable card a bit lower, so that you can see the previous card too, and if there are two cards, even lower. Those are called “fanned piles”.
Then, we want to be able to pick a card from the fanned pile that is not the top card of the pile and drag the card together with all the cards below it:
![](https://flet.dev/img/docs/solitaire-tutorial/fanned_piles3.gif)
To be able to do that, it would be useful to have the information about the pile of cards in the slot from which the card is dragged, as well as in the slot to which it is being dropped. Let’s restructure our program and get it ready for the implementation of the fanned piles.
### Slot, Card and Solitaire classes[​](https://flet.dev/docs/tutorials/python-solitaire/#slot-card-and-solitaire-classes "Direct link to Slot, Card and Solitaire classes")
A slot could have a `pile` property that would hold a list of cards that were placed there. Now the slot is a `Container` control object, and we can’t add any new properties to it. Let’s create a new `Slot` class that will inherit from `Container` and add a `pile` property to it:
```
SLOT_WIDTH =70SLOT_HEIGHT =100import flet as ftclassSlot(ft.Container):def__init__(self, top, left):super().__init__()    self.pile=[]    self.width=SLOT_WIDTH    self.height=SLOT_HEIGHT    self.left=left    self.top=top    self.border=ft.border.all(1)
```

Similarly to `Slot` class, let’s create a new `Card` class with `slot` property to remember in which slot it resides. It will inherit from `GestureDetector` and we’ll move all card-related methods to it:
```
CARD_WIDTH =70CARD_HEIGTH =100DROP_PROXIMITY =20import flet as ftclassCard(ft.GestureDetector):def__init__(self, solitaire, color):super().__init__()    self.slot =None    self.mouse_cursor=ft.MouseCursor.MOVE    self.drag_interval=5    self.on_pan_start=self.start_drag    self.on_pan_update=self.drag    self.on_pan_end=self.drop    self.left=None    self.top=None    self.solitaire = solitaire    self.color = color    self.content=ft.Container(bgcolor=self.color, width=CARD_WIDTH, height=CARD_HEIGTH)defmove_on_top(self):"""Moves draggable card to the top of the stack"""    self.solitaire.controls.remove(self)    self.solitaire.controls.append(self)    self.solitaire.update()defbounce_back(self):"""Returns card to its original position"""    self.top = self.slot.top    self.left = self.slot.left    self.update()defplace(self, slot):"""Place card to the slot"""    self.top = slot.top    self.left = slot.leftdefstart_drag(self, e: ft.DragStartEvent):    self.move_on_top()    self.update()defdrag(self, e: ft.DragUpdateEvent):    self.top =max(0, self.top + e.delta_y)    self.left =max(0, self.left + e.delta_x)    self.update()defdrop(self, e: ft.DragEndEvent):for slot in self.solitaire.slots:if(abs(self.top - slot.top)< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY):        self.place(slot)        self.update()return    self.bounce_back()    self.update()
```

note
Note: since each card has `slot` property now, there is no need to remember `start_left` and `start_top` position of the draggable card in Solitaire class anymore, because we can just bounce it back to it’s slot.
Let’s update `Solitaire` class to inherit from `Stack`, and move the creation of cards and slots there:
```
SOLITAIRE_WIDTH =1000SOLITAIRE_HEIGHT =500import flet as ftfrom slot import Slotfrom card import CardclassSolitaire(ft.Stack):def__init__(self):super().__init__()    self.controls =[]    self.slots =[]    self.cards =[]    self.width = SOLITAIRE_WIDTH    self.height = SOLITAIRE_HEIGHTdefdid_mount(self):    self.create_card_deck()    self.create_slots()    self.deal_cards()defcreate_card_deck(self):    card1 = Card(self, color="GREEN")    card2 = Card(self, color="YELLOW")    self.cards =[card1, card2]defcreate_slots(self):    self.slots.append(Slot(top=0, left=0))    self.slots.append(Slot(top=0, left=200))    self.slots.append(Slot(top=0, left=300))    self.controls.extend(self.slots)    self.update()defdeal_cards(self):    self.controls.extend(self.cards)for card in self.cards:      card.place(self.slots[0])    self.update()
```

note
If you try to call `create_slots()` and `create_card_deck()` and `deal_cards()` methods `__init__()` method of the Solitaire class, it will cause an error “Control must be added to the page first”. To fix this, we create slots and cards inside the `did_mount()` method, which happens immediately after the stack is added to the page.
Our main program will be very simple now:
```
import flet as ftfrom solitaire import Solitairedefmain(page: ft.Page):  solitaire = Solitaire()  page.add(solitaire)ft.app(main)
```

You can find the full source code for this step [here](https://github.com/flet-dev/examples/tree/main/python/tutorials/solitaire/solitaire-classes). It works exactly the same way as the proof of concept app, but re-written with the new classes to be ready for adding more complex functionality to it.
### Placing card with offset[​](https://flet.dev/docs/tutorials/python-solitaire/#placing-card-with-offset "Direct link to Placing card with offset")
When the card is being placed to a slot in the `card.place()` method, we need to do three things:
  * Remove the card from its original slot, if it exists
  * Change card’s slot to the new slot
  * Add the card to the new slot’s pile


```
defplace(self, slot):# remove card from it's original slot, if existsif self.slot isnotNone:    self.slot.pile.remove(self)# change card's slot to a new slot  self.slot = slot# add card to the new slot's pile  slot.pile.append(self)
```

When updating card’s `top` and `left` position, `left` should remain the same, but `top` will depend on the length of the new slot’s pile:
```
  self.top = slot.top +len(slot.pile)* CARD_OFFSET  self.left = slot.left
```

Now the cards are placed with offset which gives us the fanned pile look:
![](https://flet.dev/img/docs/solitaire-tutorial/fanned_piles1.png)
### Drag pile of cards[​](https://flet.dev/docs/tutorials/python-solitaire/#drag-pile-of-cards "Direct link to Drag pile of cards")
If you try to drag the card from the bottom of the pile now, it will look like this:
![](https://flet.dev/img/docs/solitaire-tutorial/fanned_piles2.gif)
To fix this problem, we need to update all the methods that work with the draggable card to work with the draggable pile instead.
Let’s create `get_draggable_pile()` method that will get the list of cards that need to be dragged together, starting with the card you picked:
```
defget_draggable_pile(self):"""returns list of cards that will be dragged together, starting with the current card"""if self.slot isnotNone:      self.draggable_pile = self.slot.pile[self.slot.pile.index(self):]else:# slot == None when the cards are dealt and need to be place in slot for the first time      self.draggable_pile =[self]
```

Then, we’ll update `move_on_top()` method:
```
defmove_on_top(self):"""Brings draggable card pile to the top of the stack"""# for card in self.get_draggable_pile():for card in self.draggable_pile:      self.solitaire.controls.remove(card)      self.solitaire.controls.append(card)    self.solitaire.update()
```

Additionally, we need to update `drag()` method to go through the draggable pile and update positions of all the cards being dragged:
```
defdrag(self, e: ft.DragUpdateEvent):for card in self.draggable_pile:      card.top =(max(0, self.top + e.delta_y)+ self.draggable_pile.index(card)* CARD_OFFSET)      card.left =max(0, self.left + e.delta_x)      self.solitaire.update()
```

Also, we need to update `place()` method to place place the draggable pile to the slot:
```
defplace(self, slot):"""Place draggable pile to the slot"""for card in self.draggable_pile:      card.top = slot.top +len(slot.pile)* CARD_OFFSET      card.left = slot.left# remove card from it's original slot, if it existsif card.slot isnotNone:        card.slot.pile.remove(card)# change card's slot to a new slot      card.slot = slot# add card to the new slot's pile      slot.pile.append(card)    self.solitaire.update()
```

Finally, if no slot in proximity is found, we need to bounce the whole pile back to its original position:
```
defbounce_back(self):"""Returns draggable pile to its original position"""for card in self.draggable_pile:      card.top = card.slot.top + card.slot.pile.index(card)* CARD_OFFSET      card.left = card.slot.left    self.solitaire.update()
```

The full source code of this step can be found [here](https://github.com/flet-dev/examples/tree/main/python/tutorials/solitaire/solitaire-fanned-piles). Now we can drag and drop cards in fanned piles, which means we are ready for the real deal!
## Solitaire setup[​](https://flet.dev/docs/tutorials/python-solitaire/#solitaire-setup "Direct link to Solitaire setup")
Let’s take a look at the [wikipedia article about Klondike (solitaire)](https://en.wikipedia.org/wiki/Klondike_\(solitaire\)#Rules):
> Klondike is played with a standard 52-card deck.
> After shuffling, a tableau of seven fanned piles of cards is laid from left to right. From left to right, each pile contains one more card than the last. The first and left-most pile contains a single upturned card, the second pile contains two cards, the third pile contains three cards, the fourth pile contains four cards, the fifth pile contains five cards, the sixth pile contains six cards, and the seventh pile contains seven cards. The topmost card of each pile is turned face up. The remaining cards form the stock and are placed facedown at the upper left of the layout.
> The four foundations (light rectangles in the upper right of the figure) are built up by suit from Ace (low in this game) to King, and the tableau piles can be built down by alternate colors.
![](https://flet.dev/img/docs/solitaire-tutorial/game_setup_wiki.png)
We will now work on this setup step by step.
### Create card deck[​](https://flet.dev/docs/tutorials/python-solitaire/#create-card-deck "Direct link to Create card deck")
The first step is to create a full deck of cards in Solitaire class. Each card should have a `suit` property (hearts, diamonds, clubs and spades) and a `rank` property (from Ace to King). For the suit, its `color` is important, because tableau piles are built by alternate colors.
For the rank, its `value` is important, because foundations are built from the lowest (Ace) to the highest (King) rank value.
In solitaire.py, create `Suite` and `Rank` classes:
```
classSuite:def__init__(self, suite_name, suite_color):    self.name = suite_name    self.color = suite_colorclassRank:def__init__(self, card_name, card_value):    self.name = card_name    self.value = card_value
```

Now, in the `Card` class, instead of accepting the color as an argument, we’ll be accepting `suite` and `rank` in `__init__()`. Additionally, we’ll add `face_up` property to the card and the Container will now has image of the back of the card as its `content`:
```
classCard(ft.GestureDetector):def__init__(self, solitaire, suite, rank):super().__init__()    self.mouse_cursor=ft.MouseCursor.MOVE    self.drag_interval=5    self.on_pan_start=self.start_drag    self.on_pan_update=self.drag    self.on_pan_end=self.drop    self.suite=suite    self.rank=rank    self.face_up=False    self.top=None    self.left=None    self.solitaire = solitaire    self.slot =None    self.content=ft.Container(      width=CARD_WIDTH,      height=CARD_HEIGTH,      border_radius = ft.border_radius.all(6),      content=ft.Image(src="card_back.png"))
```

All the images for the face up cards, as well as card back are stored in the “images” folder in the same directory as main.py.
note
For the reference to the image file to work, we need to specify the folder were it resides in the assets_dir in main.py:
```
ft.app(main, assets_dir="images")
```

Finally, in `solitaire.create_card_deck()` we'll create lists of suites and ranks and then the 52-card deck:
```
defcreate_card_deck(self):  suites =[    Suite("hearts","RED"),    Suite("diamonds","RED"),    Suite("clubs","BLACK"),    Suite("spades","BLACK"),]  ranks =[    Rank("Ace",1),    Rank("2",2),    Rank("3",3),    Rank("4",4),    Rank("5",5),    Rank("6",6),    Rank("7",7),    Rank("8",8),    Rank("9",9),    Rank("10",10),    Rank("Jack",11),    Rank("Queen",12),    Rank("King",13),]  self.cards =[]for suite in suites:for rank in ranks:      self.cards.append(Card(solitaire=self, suite=suite, rank=rank))
```

The card deck is ready to be dealt, and now we need to create the layout for it.
### Create slots[​](https://flet.dev/docs/tutorials/python-solitaire/#create-slots "Direct link to Create slots")
Klondike solitaire game layout should look like this:
![](https://flet.dev/img/docs/solitaire-tutorial/solitaire-layout.svg)
Let’s create all those slots in `solitaire.create_slots()`:
```
defcreate_slots(self):  self.stock = Slot(top=0, left=0, border=ft.border.all(1))  self.waste = Slot(top=0, left=100, border=None)  self.foundations =[]  x =300for i inrange(4):    self.foundations.append(Slot(top=0, left=x, border=ft.border.all(1,"outline")))    x +=100  self.tableau =[]  x =0for i inrange(7):    self.tableau.append(Slot(top=150, left=x, border=None))    x +=100  self.controls.append(self.stock)  self.controls.append(self.waste)  self.controls.extend(self.foundations)  self.controls.extend(self.tableau)  self.update()
```

note
Note: some slots should have visible border and some shouldn’t, so we added border to the list of arguments for the creation of `Slot` objects.
### Deal cards[​](https://flet.dev/docs/tutorials/python-solitaire/#deal-cards "Direct link to Deal cards")
Let's start with shuffling the cards and adding them to the list of controls:
```
defdeal_cards(self):  random.shuffle(self.cards)  self.controls.extend(self.cards)  self.update()
```

Then we'll deal the cards to the tableau piles from left to right so that each pile contains one more card than the last, and place the remaining cards to the stock pile:
```
defdeal_cards(self):  random.shuffle(self.cards)  self.controls.extend(self.cards)# deal to tableau  first_slot =0  remaining_cards = self.cardswhile first_slot <len(self.tableau):for slot in self.tableau[first_slot:]:      top_card = remaining_cards[0]      top_card.place(slot)      remaining_cards.remove(top_card)    first_slot +=1# place remaining cards to stock pilefor card in remaining_cards:    card.place(self.stock)  self.update()
```

Let’s run the program and see where we are at now:
![](https://flet.dev/img/docs/solitaire-tutorial/game_setup1.png)
Cards in stock were placed in a fanned pile in the same manner as to the tableau, but they should have been placed to a regular pile instead. To fix this problem, let’s add this condition to the `card.place()` method:
```
defplace(self, slot):"""Place draggable pile to the slot"""if slot in self.solitaire.tableau:    self.top = slot.top +len(slot.pile)* self.solitaire.card_offsetelse:    self.top = slot.top  self.left = slot.left
```

Now cards are only placed in fanned piles to tableau:
![](https://flet.dev/img/docs/solitaire-tutorial/game_setup2.png)
If you try moving the cards around now, the program won’t work. The reason for this is that in the `card.drop()` method iterates through list of slots which we don’t have now.
Let’s update the method to go separately through foundations and tableau:
```
defdrop(self, e: ft.DragEndEvent):for slot in self.solitaire.tableau:if(abs(self.top -(slot.top +len(slot.pile)* CARD_OFFSET))< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY):      self.place(slot)      self.solitaire.update()returnfor slot in self.solitaire.foundations:if(abs(self.top - slot.top)< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY):      self.place(slot)      self.solitaire.update()return  self.bounce_back()
```

### Reveal top cards in tableau piles[​](https://flet.dev/docs/tutorials/python-solitaire/#reveal-top-cards-in-tableau-piles "Direct link to Reveal top cards in tableau piles")
Now we have the correct game setup and as a last touch we need to reveal the topmost cards in tableau piles.
In `Slot` class, create a `get_top_card()` method:
```
defget_top_card(self):iflen(self.pile)>0:return self.pile[-1]
```

In `Card` class, create `turn_dace_up()` method:
```
defturn_face_up(self):  self.face_up =True  self.content.content.src=f"/images/{self.rank.name}_{self.suite.name}.svg"  self.solitaire.update()
```

Finally, reveal the topmost cards in the `solitaire.deal_cards()`:
```
for slot in self.tableau:  slot.get_top_card().turn_face_up()  self.update()
```

Let’s see how it looks now:
![](https://flet.dev/img/docs/solitaire-tutorial/game_setup3.png)
The full source code for this step can be found [here](https://github.com/flet-dev/examples/tree/main/python/tutorials/solitaire/solitaire-game-setup).
Congratulations on completing the Solitaire game setup! You’ve created a full 52-card deck, built layout with stock, waste, foundations and tableau piles, dealt the cards and revealed the top cards in tableau. Let’s move on to the next item on our todo list, which is Solitaire Rules.
## Solitaire rules[​](https://flet.dev/docs/tutorials/python-solitaire/#solitaire-rules "Direct link to Solitaire rules")
If you run your current version of Solitaire, you’ll notice that you can do some crazy things with your cards:
![](https://flet.dev/img/docs/solitaire-tutorial/game_rules1.gif)
Now it is time to implement some rules.
### General rules[​](https://flet.dev/docs/tutorials/python-solitaire/#general-rules "Direct link to General rules")
Currently, we can move any card, but only face-up cards should be moved. Let’s add this check in `start_drag`, `drag` and `drop` methods of the card:
```
defstart_drag(self, e: ft.DragStartEvent):if self.face_up:    self.move_on_top()    self.solitaire.update()defdrag(self, e: ft.DragUpdateEvent):if self.face_up:for card in self.draggable_pile:      card.top =max(0, self.top + e.delta_y)+ self.draggable_pile.index(card)* CARD_OFFSET      card.left =max(0, self.left + e.delta_x)      card.solitaire.update()defdrop(self, e: ft.DragEndEvent):if self.face_up:for slot in self.solitaire.tableau:if(abs(self.top -(slot.top +len(slot.pile)* CARD_OFFSET))< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY):        self.place(slot)returnfor slot in self.solitaire.foundations:if(abs(self.top - slot.top)< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY):        self.place(slot)return  self.bounce_back()
```

Now let’s specify `click` method for the `on_tap` event of the card to reveal the card if you click on a faced-down top card in a tableau pile:
```
defclick(self, e):if self.slot in self.solitaire.tableau:ifnot self.face_up and self == self.slot.get_top_card():      self.turn_face_up()      self.solitaire.update()
```

Let's check how it works:
![](https://flet.dev/img/docs/solitaire-tutorial/game_rules2.gif)
### Foundations rules[​](https://flet.dev/docs/tutorials/python-solitaire/#foundations-rules "Direct link to Foundations rules")
At the moment we can place fanned piles to foundations, which shouldn’t be allowed. Let’s check the draggable pile length to fix it:
```
defdrop(self, e: ft.DragEndEvent):for slot in self.solitaire.tableau:if(abs(self.top -(slot.top +len(slot.pile)* CARD_OFFSET))< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY):      self.place(slot)returniflen(self.draggable_pile)==1:for slot in self.solitaire.foundations:if(abs(self.top - slot.top)< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY):        self.place(slot)return  self.bounce_back()
```

Then, of course, not any card can be placed to a foundation. According to the rules, a foundation should start with an Ace and then the cards of the same suite can be placed on top of it to build a pile form Ace to King.
Let’s add this rule to Solitaire class:
```
defcheck_foundations_rules(self, card, slot):  top_card = slot.get_top_card()if top_card isnotNone:return(      card.suite.name == top_card.suite.nameand card.rank.value - top_card.rank.value ==1)else:return card.rank.name =="Ace"
```

We’ll check this rule in `drop()` method before placing a card to a foundation slot:
```
defdrop(self, e: ft.DragEndEvent):if self.face_up:for slot in self.solitaire.tableau:if(abs(self.top -(slot.top +len(slot.pile)* CARD_OFFSET))< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY):        self.place(slot)returniflen(self.draggable_pile)==1:for slot in self.solitaire.foundations:if(abs(self.top - slot.top)< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY)and self.solitaire.check_foundations_rules(self, slot):          self.place(slot)return    self.bounce_back()
```

As a final touch for foundations rules, let’s implement `doublclick` method for `on_double_tap` event of a card. It will be checking if the faced-up card fits into any of the foundations and place it there:
```
def double-click(self, e):    self.get_draggable_pile()if self.face_up andlen(self.draggable_pile ==1):      self.move_on_top()for slot in self.solitaire.foundations:if self.solitaire.check_foundations_rules(self, slot):          self.place(slot)return
```

### Tableau rules[​](https://flet.dev/docs/tutorials/python-solitaire/#tableau-rules "Direct link to Tableau rules")
Finally, let's implement the rules to build tableau piles down from King to Ace by alternating suite color. Additionally, only King can be placed to an empty tableau slot.
Let’s add these rules for Solitaire class:
```
defcheck_tableau_rules(self, card, slot):  top_card = slot.get_top_card()if top_card isnotNone:return(      card.suite.color != top_card.suite.colorand top_card.rank.value - card.rank.value ==1and top_card.face_up)else:return card.rank.name =="King"
```

Similarly to the foundations rules, we’ll check tableau rules before placing a card to a tableau pile:
```
defdrop(self, e: ft.DragEndEvent):if self.face_up:for slot in self.solitaire.tableau:if(abs(self.top -(slot.top +len(slot.pile)* CARD_OFFSET))< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY)and self.solitaire.check_tableau_rules(self, slot):        self.place(slot)returniflen(self.draggable_pile)==1:for slot in self.solitaire.foundations:if(abs(self.top - slot.top)< DROP_PROXIMITYandabs(self.left - slot.left)< DROP_PROXIMITY)and self.solitaire.check_foundations_rules(self, slot):          self.place(slot)return    self.bounce_back()
```

### Stock and waste[​](https://flet.dev/docs/tutorials/python-solitaire/#stock-and-waste "Direct link to Stock and waste")
To properly play Solitaire game right now we are missing the remaining cards that are piled in the stock.
Let’s update `click()` method of the card to go through the stock pile and place the cards to waste as we go:
```
defclick(self, e):if self.slot in self.solitaire.tableau:ifnot self.face_up and self == self.slot.get_top_card():      self.turn_face_up()elif self.slot == self.solitaire.stock:    self.move_on_top()    self.place(self.solitaire.waste)    self.turn_face_up()
```

That’s it! Now you can properly play solitaire, but it very difficult to win the game if you cannot pass though the waste again. Let’s implement `click()` for `on_click` event of the stock Slot to go thought the stock pile again:
```
classSlot(ft.Container):def__init__(self, solitaire, top, left, border):super().__init__()    self.pile=[]    self.width=SLOT_WIDTH    self.height=SLOT_HEIGHT    self.left=left    self.top=top    self.on_click=self.click    self.solitaire=solitaire    self.border=border    self.border_radius = ft.border_radius.all(6)defclick(self, e):if self == self.solitaire.stock:      self.solitaire.restart_stock()
```

`restart_stock()` method in `Solitaire` class will place all cards from waste to stock again:
```
defrestart_stock(self):whilelen(self.waste.pile)>0:    card = self.waste.get_top_card()    card.turn_face_down()    card.move_on_top()    card.place(self.stock)
```

For `card.place()` method to work properly with cards from Stock and Waste, we’ve added a condition to `card.get_draggable_pile()`, so that it returns the top card only and not the whole pile:
```
defget_draggable_pile(self):"""returns list of cards that will be dragged together, starting with the current card"""if(      self.slot isnotNoneand self.slot != self.solitaire.stockand self.slot != self.solitaire.waste):      self.draggable_pile = self.slot.pile[self.slot.pile.index(self):]else:# slot == None when the cards are dealt and need to be place in slot for the first time      self.draggable_pile =[self]
```

All done! The full source code for this step can be found [here](https://github.com/flet-dev/examples/tree/main/python/tutorials/solitaire/solitaire-game-rules).
Let’s move on to the last step of the game itself - detecting the situation when you have won.
## Winning the game[​](https://flet.dev/docs/tutorials/python-solitaire/#winning-the-game "Direct link to Winning the game")
According to [wikipedia](https://en.wikipedia.org/wiki/Klondike_\(solitaire\)#Probability_of_winning), some suggest the chances of winning the game as being 1 in 30 games.
Knowing that the chances of winning are quite low, we should plan on showing the user something exciting when that finally happens.
First, let’s add a check for the winning condition to `Solitaire` class. If all four foundations contain total of 52 cards, then you have won:
```
defcheck_win(self):  cards_num =0for slot in self.foundations:    cards_num +=len(slot.pile)if cards_num ==52:returnTruereturnFalse
```

We’ll be checking if this condition is true each time a card is placed to a foundation:
```
defplace(self, slot):"""Place draggable pile to the slot"""  draggable_pile = self.get_draggable_pile()for card in draggable_pile:if slot in self.solitaire.tableau:      card.top = slot.top +len(slot.pile)* CARD_OFFSETelse:      card.top = slot.top    card.left = slot.left# remove card from it's original slot, if existsif card.slot isnotNone:      card.slot.pile.remove(card)# change card's slot to a new slot    card.slot = slot# add card to the new slot's pile    slot.pile.append(card)if self.solitaire.check_win():    self.solitaire.winning_sequence()  self.solitaire.update()
```

Finally, if the winning condition is met, it will trigger a winning sequence involving [position animation](https://flet.dev/docs/cookbook/animations#position-animation):
```
defwinning_sequence(self):for slot in self.foundations:for card in slot.pile:      card.animate_position=1000      card.move_on_top()      card.top = random.randint(0, SOLITAIRE_HEIGHT)      card.left = random.randint(0, SOLITAIRE_WIDTH)      self.update()  self.controls.append(ft.AlertDialog(title=ft.Text("Congratulations! You won!"),open=True))
```

![](https://flet.dev/img/docs/solitaire-tutorial/winning_the_game.gif)
Wow! We did it. You can find the full source code for the Solitaire game [here](https://github.com/flet-dev/examples/tree/main/python/tutorials/solitaire/solitaire-final-part1).
Now, as we have a decent desktop version of the game, let’s deploy it as a web app to share with your friends and colleagues.
## Deploying the app[​](https://flet.dev/docs/tutorials/python-solitaire/#deploying-the-app "Direct link to Deploying the app")
Congratulations! You have created your Solitaire game app in Python with Flet, and it looks awesome!
Now it's time to share your app with the world!
[Follow these instructions](https://flet.dev/docs/publish/web) to deploy your Flet app as a web app to Fly.io or Replit.
## Summary[​](https://flet.dev/docs/tutorials/python-solitaire/#summary "Direct link to Summary")
In this tutorial, you have learnt how to:
  * [Create](https://flet.dev/docs/getting-started/create-flet-app) a simple Flet app;
  * Drag and drop cards with [GestureDetector](https://flet.dev/docs/controls/gesturedetector);
  * [Create your own classes](https://flet.dev/docs/getting-started/custom-controls) that inherit from Flet controls;
  * Design UI layout using absolute positioning of controls in [Stack](https://flet.dev/docs/controls/stack);
  * Implement [implicit animations](https://flet.dev/docs/cookbook/animations);
  * [Deploy](https://flet.dev/docs/publish/web) your Flet app to the web;


For further reading you can explore [controls](https://flet.dev/docs/controls) and [examples repository](https://github.com/flet-dev/examples/tree/main/python).
We would love to hear your feedback! Please drop us an email, join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/tutorials/python-solitaire.md)
[PreviousTrello clone](https://flet.dev/docs/tutorials/trello-clone)[NextChat app](https://flet.dev/docs/tutorials/python-chat)
  * [Getting started with Flet](https://flet.dev/docs/tutorials/python-solitaire/#getting-started-with-flet)
  * [Proof of concept app for draggable cards](https://flet.dev/docs/tutorials/python-solitaire/#proof-of-concept-app-for-draggable-cards)
    * [Step 1: Drag the card around](https://flet.dev/docs/tutorials/python-solitaire/#step-1-drag-the-card-around)
    * [Step 2: Drop the card in the slot or bounce it back](https://flet.dev/docs/tutorials/python-solitaire/#step-2-drop-the-card-in-the-slot-or-bounce-it-back)
    * [Step 3: Adding a second card](https://flet.dev/docs/tutorials/python-solitaire/#step-3-adding-a-second-card)
    * [Step 4: Adding more slots](https://flet.dev/docs/tutorials/python-solitaire/#step-4-adding-more-slots)
  * [Fanned card piles](https://flet.dev/docs/tutorials/python-solitaire/#fanned-card-piles)
    * [Slot, Card and Solitaire classes](https://flet.dev/docs/tutorials/python-solitaire/#slot-card-and-solitaire-classes)
    * [Placing card with offset](https://flet.dev/docs/tutorials/python-solitaire/#placing-card-with-offset)
    * [Drag pile of cards](https://flet.dev/docs/tutorials/python-solitaire/#drag-pile-of-cards)
  * [Solitaire setup](https://flet.dev/docs/tutorials/python-solitaire/#solitaire-setup)
    * [Create card deck](https://flet.dev/docs/tutorials/python-solitaire/#create-card-deck)
    * [Create slots](https://flet.dev/docs/tutorials/python-solitaire/#create-slots)
    * [Deal cards](https://flet.dev/docs/tutorials/python-solitaire/#deal-cards)
    * [Reveal top cards in tableau piles](https://flet.dev/docs/tutorials/python-solitaire/#reveal-top-cards-in-tableau-piles)
  * [Solitaire rules](https://flet.dev/docs/tutorials/python-solitaire/#solitaire-rules)
    * [General rules](https://flet.dev/docs/tutorials/python-solitaire/#general-rules)
    * [Foundations rules](https://flet.dev/docs/tutorials/python-solitaire/#foundations-rules)
    * [Tableau rules](https://flet.dev/docs/tutorials/python-solitaire/#tableau-rules)
    * [Stock and waste](https://flet.dev/docs/tutorials/python-solitaire/#stock-and-waste)
  * [Winning the game](https://flet.dev/docs/tutorials/python-solitaire/#winning-the-game)
  * [Deploying the app](https://flet.dev/docs/tutorials/python-solitaire/#deploying-the-app)
  * [Summary](https://flet.dev/docs/tutorials/python-solitaire/#summary)


Docs
  * [Introduction](https://flet.dev/docs)
  * [Controls reference](https://flet.dev/docs/controls)


Community
  * [Discord](https://discord.gg/dzWXP8SHG8)
  * [Stack Overflow](https://stackoverflow.com/questions/tagged/flet)
  * [X](https://x.com/fletdev)
  * [Bluesky](https://bsky.app/profile/fletdev.bsky.social)


More
  * [Blog](https://flet.dev/blog)
  * [GitHub](https://github.com/flet-dev/flet)
  * [Support](https://flet.dev/support)


Legal
  * [Privacy policy](https://flet.dev/privacy-policy)


Copyright © 2025 Appveyor Systems Inc. Built with Docusaurus.
