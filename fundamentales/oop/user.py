class User():
    def __int__(self,first_name,last_name,email,age,is_reward_member=False,gold_card_points=0  ):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_reward_member=is_reward_member
        self.gold_card_points=gold_card_points
    def display_info(self):
    def display_info(self):
        
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
    def enrol(self):
        self.is_reward_member=True
        self.gold_card_points=200
        return self
    def spend_points(self,amount):
        if(self.gold_card_points>=amount):
            self.gold_card_points-=amount
    my_user = User("Sadie", "Flick", "sflick@codingdojo.com", 99)
    display_info(my_user)

