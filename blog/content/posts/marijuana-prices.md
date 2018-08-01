Title: Marijuana Prices in the United States
Description: Visualizing the price per gram of marijuana in the United States by quality and year.
Slug: marijuana-prices
Date: 2014-01-01 22:49
Modified: 2015-02-20 22:49
Author: Renzo Lucioni
Tags: visualization, marijuana

In November, landmark votes significantly eased marijuana laws in Colorado and Washington State. Today, Colorado becomes the first state in the nation to permit the sale and use of marijuana for recreational purposes. Washington State expects to begin legal marijuana sales this spring. 

In light of these recent developments, I was curious about how the price of marijuana has changed nationally over the last few years. Using crowdsourced transaction data collected anonymously by [priceofweed.com](http://www.priceofweed.com/) and made available by Zachary M. Jones on [GitHub](https://github.com/zmjones/priceofweed), I assembled the following series of twelve choropleth maps. Note that the prices shown here most likely correspond to bulk purchases.

![Choropleth maps of historical marijuana prices in the US]({filename}../images/marijuana-prices.png)

Prices for high quality marijuana appear to be consistently lowest closer to the West Coast, and have dropped considerably since 2010. As of 2013, one gram of high quality marijuana can be most cheaply purchased in Washington State, Oregon, or Colorado. A single gram of high quality marijuana appears to be most expensive in North Dakota.

In 2010, medium quality marijuana appears to have been cheapest in the South. Since then, prices have become more uniform. As of 2013, one gram of medium quality marijuana can be most cheaply purchased in Washington State, Oregon, California, or Colorado, but also in Mississippi, Alabama, or South Carolina.

The price of a single gram of low quality marijuana appears to be consistently lowest in the South and Southwest. More recently, cheap, low quality marijuana can also be found in Washington State, California, Montana, Wisconsin, Ohio, Vermont, or Delaware.

My code, raw images (SVG and PNG), and all associated data can be found on [GitHub](https://github.com/rlucioni/viz/tree/master/marijuana). A brief technical note: I manually colored these maps, using Python to determine which hex color codes to use for each state. In retrospect, D3 would have been a better tool for this job, and I would have used it had I been more familar with it at the time.  

On January 6, 2014, *The Washington Post* featured these choropleth maps in an article on its [GovBeat](http://www.washingtonpost.com/blogs/govbeat/wp/2014/01/06/how-much-does-marijuana-cost-in-the-u-s/) blog.
