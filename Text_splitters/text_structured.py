from langchain.text_splitter import RecursiveCharacterTextSplitter


text = """
The minimum registration term allowed for .
ai domains is 2 through 10 years for registration and renewal, and a 2-year renewal for domain transfer.
[7] Identity Digital is the authority in charge of managing this extension. Registrations began on 16 February 1995. The limits on the number of characters used for the domain name are, at a minimum, from 1 to 3, depending on the registrar, and always at most 63 characters.[a] The character set supported for .ai domain names includes A–Z, a–z, 0–9, and hyphen. As of November 2022, .ai domains cannot accommodate IDN characters.[9] There are no requirements for registering a domain, including local and foreign residents.[7]

A .ai domain can be suspended or revoked, if the domain is involved in illegal activity such as violating trademarks or copyrights. 
Usage must not violate the laws of Anguilla.[12]

Anguilla uses the UDRP. Filing a UDRP challenge requires using one of the ICANN Approved Dispute Resolution Service Providers. 
If the domain is with an ICANN accredited registrar, they should work with the arbitrator. Usually this means either doing nothing or transferring a domain. .ai domains are transferable to any desired registrars as the registration of domain is done maintaining EPP.[13]

There used to be a whois.ai-based platform of expired domains in which those could be procured and auctioned every ten days through a standard online process.
[14] The last auctions of such kind closed there in December 2024; the platform had been scheduled for shutdown on 30 June 2025.[15] As of 10 July 2025, it is still online.[16][17][18]

Valuation
Domains cost depends on the registrar, with yearly fees ranging from US$140 (the base fee, as established by Anguilla) to $200.[19][20] As of July 2025, the highest-valued .
ai domain is an undisclosed one sold on 8 November 2023, on Escrow.com, for US$1,500,000—months after an initial $300,000 sale to the same buyer.[21] Among the publicly disclosed ones, the most valued, fin.ai, was sold for $1,000,000 in March 2025.[22][23]

On 16 December 2017, the .ai registry started supporting the Extensible Provisioning Protocol (EPP) and migrated all of its domains onto an EPP system.
[24][25] Consequently, many registrars are allowed to sell .ai domains. Since that date, the .ai ccTLD has also been popular with artificial intelligence companies and organizations. Though such trends are primarily seen among new AI based companies or startups, many established AI and Tech companies preferred not to opt for .ai domains. For example, DeepMind has its domain retained at .com; Meta has redirected its facebook.ai domain to ai.meta.com.[26]
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size= 200,
    chunk_overlap= 20,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(text)

print('------------------------------------------------')
print(len(chunks))
print('------------------------------------------------')
print(chunks[3])
print('------------------------------------------------')
print(chunks)