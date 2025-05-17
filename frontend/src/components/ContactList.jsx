import ContactCard from "./ContactCard";
import GroupCard from "./GroupCard";

function ContactList({ contacts,searched }) {
  return (
    <div className="container my-4">
      {contacts.length === 0 && searched && (
        <p className="text-center text-muted">No contacts found.</p>
      )}
      {contacts.map((contact, idx) => (
        contact?.source=='group' ? <GroupCard contact={contact} idx={idx}/> : <ContactCard contact={contact} idx={idx}/>
      ))}
    </div>
  );
}

export default ContactList;
