"""
STEP 1: DATA MODELS
==================
This file defines the structure of our data - like a blueprint for a house.
Each model represents a type of information we need to store.

Think of models as forms you fill out:
- Kitchen model = information about each home kitchen
- MenuItem model = information about each dish
- Order model = information about customer orders
- Review model = information about customer reviews
- User model = information about customers
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ============================================================================
# 1. USER MODEL - Stores customer information
# ============================================================================
class User(BaseModel):
    """Customer who orders food"""
    user_id: Optional[str] = None  # Auto-generated ID
    name: str  # Customer name
    email: str  # Email address
    phone: str  # Phone number
    address: str  # Delivery address
    location: dict = Field(default_factory=dict)  # {"latitude": 0, "longitude": 0}
    created_at: Optional[datetime] = None


# ============================================================================
# 2. KITCHEN MODEL - Stores home kitchen information
# ============================================================================
class Kitchen(BaseModel):
    """A home kitchen run by a mother/family"""
    kitchen_id: Optional[str] = None  # Auto-generated ID
    name: str  # Kitchen name (e.g., "Priya's Home Kitchen")
    owner_name: str  # Owner's name (mother's name)
    description: str  # About this kitchen
    cuisine_type: str  # Type of Indian food (e.g., "North Indian", "South Indian", "Gujarati")
    
    # Location information for "nearby" feature
    location: dict = Field(default_factory=dict)  # {"latitude": 0, "longitude": 0}
    address: str  # Full address
    
    # Rating and review information for AI recommendations
    average_rating: float = 0.0  # Average of all reviews (0.0 to 5.0)
    total_reviews: int = 0  # Number of reviews
    total_orders: int = 0  # Number of orders completed
    
    # Kitchen status
    is_active: bool = True  # Is kitchen open for orders?
    opening_time: str = "09:00"  # Opening time
    closing_time: str = "22:00"  # Closing time
    
    # Cultural information (for foreigners to learn about India)
    tradition_info: str = ""  # Information about traditions
    speciality: str = ""  # What makes this kitchen special
    hospitality_note: str = ""  # Message about Indian hospitality
    
    image_url: Optional[str] = None  # Profile/Cover photo of the kitchen
    created_at: Optional[datetime] = None


# ============================================================================
# 3. MENU ITEM MODEL - Stores dish information
# ============================================================================
class MenuItem(BaseModel):
    """A dish/food item from a kitchen"""
    item_id: Optional[str] = None  # Auto-generated ID
    kitchen_id: str  # Which kitchen serves this dish
    
    name: str  # Dish name (e.g., "Butter Chicken")
    description: str  # Description of the dish
    price: float  # Price in your currency
    
    # Food category
    category: str  # "Main Course", "Appetizer", "Dessert", "Beverage"
    cuisine_style: str  # "Punjabi", "Gujarati", "South Indian", etc.
    
    # For trending food feature
    order_count: int = 0  # How many times ordered (for trending)
    is_available: bool = True  # Is it available now?
    
    # Cultural information
    origin_region: str = ""  # Which part of India this dish is from
    cultural_significance: str = ""  # Why this dish is special
    
    image_url: Optional[str] = None  # Photo of the dish
    spice_level: int = 2  # 1=Mild, 2=Medium, 3=Hot, 4=Very Hot
    preparation_time: int = 30  # Minutes to prepare


# ============================================================================
# 4. REVIEW MODEL - Stores customer reviews
# ============================================================================
class Review(BaseModel):
    """Customer review for a kitchen"""
    review_id: Optional[str] = None  # Auto-generated ID
    kitchen_id: str  # Which kitchen is being reviewed
    user_id: str  # Who wrote the review
    user_name: str  # Reviewer's name
    
    rating: int = Field(ge=1, le=5)  # Rating from 1 to 5 stars
    comment: str  # Review text
    
    # What they liked
    liked_food: List[str] = []  # Which dishes they liked
    experience: str = ""  # Their overall experience
    
    created_at: Optional[datetime] = None


# ============================================================================
# 5. ORDER MODEL - Stores customer orders
# ============================================================================
class Order(BaseModel):
    """Customer order"""
    order_id: Optional[str] = None  # Auto-generated ID
    user_id: str  # Who placed the order
    kitchen_id: str  # Which kitchen
    
    # Order items: list of dishes ordered
    items: List[dict] = []  # [{"item_id": "123", "name": "Butter Chicken", "quantity": 2, "price": 15.99}]
    
    # Pricing
    subtotal: float  # Total before taxes
    tax: float  # Tax amount
    delivery_fee: float  # Delivery charge
    total_amount: float  # Final total
    
    # Delivery information
    delivery_address: str  # Where to deliver
    delivery_location: dict = Field(default_factory=dict)  # {"latitude": 0, "longitude": 0}
    
    # Order status
    status: str = "pending"  # "pending", "confirmed", "preparing", "ready", "out_for_delivery", "delivered", "cancelled"
    
    # Timestamps
    ordered_at: Optional[datetime] = None
    estimated_delivery: Optional[datetime] = None


# ============================================================================
# 6. CART MODEL - Shopping cart (temporary, before checkout)
# ============================================================================
class CartItem(BaseModel):
    """Item in shopping cart"""
    item_id: str
    kitchen_id: str
    name: str
    price: float
    quantity: int = 1


class Cart(BaseModel):
    """Shopping cart for a user"""
    user_id: str
    kitchen_id: Optional[str] = None  # All items should be from same kitchen
    items: List[CartItem] = []
    total: float = 0.0



